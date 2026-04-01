from __future__ import annotations

import copy
import csv
import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from fnmatch import fnmatch
import getpass
from pathlib import Path
from typing import Any

from .evds_catalog import EVDSCatalogRecord, build_catalog_index, ensure_catalog_entry
from .llm import DisabledLLMClient, LLMClient
from .notebook_analysis import (
    NotebookAnalysisResult,
    TickerAnalysis,
    UNRESOLVED,
    apply_context_titles,
    build_notebook_analysis,
    family_of,
)
from .records import (
    Record,
    normalize_indicator_input,
    normalize_memory_rule_input,
    normalize_proposal_input,
    normalize_series_input,
    normalize_theme_input,
    validate_record,
    split_list,
)
from .storage import RegistryPaths, delete_record, load_catalog, load_memory_rules, load_proposals, load_record, load_registry, write_record


@dataclass(slots=True)
class InferenceArtifacts:
    analysis_result: NotebookAnalysisResult
    proposals: list[Record]


@dataclass(slots=True)
class AutoApproveSummary:
    approved: int = 0
    manual_review: int = 0
    skipped: int = 0


@dataclass(slots=True)
class ImpliedProposalSummary:
    created: int = 0
    skipped_existing: int = 0


def apply_catalog_and_memory(
    result: NotebookAnalysisResult,
    catalog_records: dict[str, Record],
    memory_rules: dict[str, Record],
) -> NotebookAnalysisResult:
    enriched = copy.deepcopy(result)
    for item in enriched.analyses:
        note_parts = [item.notes] if item.notes else []
        catalog_record = catalog_records.get(item.ticker)
        if catalog_record:
            catalog_title = str(catalog_record.get("title") or "").strip()
            if catalog_title:
                item.official_series_name = catalog_title
                note_parts.append(f"Catalog metadata applied from {catalog_record['id']}.")
            if not item.notebook_label:
                item.notebook_label = str(catalog_record.get("title") or "")
            if (not item.frequency or item.frequency == "unknown") and catalog_record.get("frequency"):
                item.frequency = str(catalog_record.get("frequency") or item.frequency)
            if (not item.unit or item.unit == "unknown") and catalog_record.get("unit") not in {"", "unknown", None}:
                item.unit = str(catalog_record.get("unit") or item.unit)
        matched_rules = find_matching_memory_rules(memory_rules.values(), item.ticker, enriched.spec_slug, "series")
        for rule in matched_rules:
            if rule.get("resolved_title") and not (catalog_record and str(catalog_record.get("title") or "").strip()):
                item.official_series_name = str(rule.get("resolved_title"))
                if not item.notebook_label:
                    item.notebook_label = str(rule.get("resolved_title"))
            if rule.get("resolved_unit"):
                item.unit = str(rule.get("resolved_unit"))
            if rule.get("resolved_frequency"):
                item.frequency = str(rule.get("resolved_frequency"))
            if rule.get("resolved_role") and str(rule.get("scope") or "global") == "notebook_slug":
                item.notebook_role = str(rule.get("resolved_role"))
            resolved_theme_ids = split_list(rule.get("resolved_theme_ids"))
            if resolved_theme_ids:
                item.linked_theme_ids = tuple(sorted(set(item.linked_theme_ids) | set(resolved_theme_ids)))
            note_parts.append(f"Memory rule applied: {rule['id']}.")
        item.notes = " ".join(part for part in note_parts if part).strip()
    enriched.analyses = apply_context_titles(enriched.analyses)
    enriched.unresolved_items = [item.ticker for item in enriched.analyses if item.official_series_name == UNRESOLVED]
    return enriched


def find_matching_memory_rules(rules: list[Record] | Any, ticker: str, notebook_slug: str, target_type: str) -> list[Record]:
    matched: list[Record] = []
    for rule in rules:
        if rule.get("record_type") != "memory_rule":
            continue
        if rule.get("target_type") not in {"", target_type}:
            continue
        scope = str(rule.get("scope") or "global")
        pattern = str(rule.get("match_pattern") or "")
        if not pattern:
            continue
        identifiers = {ticker, f"evds:{ticker}", family_of(ticker)}
        if scope == "notebook_slug" and str(rule.get("notebook_slug") or "") != notebook_slug:
            continue
        if scope == "family":
            if family_of(ticker) != pattern and not fnmatch(ticker, pattern):
                continue
        elif not any(fnmatch(identifier, pattern) for identifier in identifiers):
            continue
        matched.append(rule)
    scope_rank = {"notebook_slug": 0, "family": 1, "global": 2}
    return sorted(matched, key=lambda item: (scope_rank.get(str(item.get("scope") or "global"), 3), item["id"]))


def infer_notebook_semantics(
    notebook_path: str | Path,
    spec: str,
    paths: RegistryPaths,
    llm_client: LLMClient | None = None,
) -> InferenceArtifacts:
    base_result = build_notebook_analysis(notebook_path, spec=spec)
    catalog = load_catalog(paths)
    catalog_index = build_catalog_index(catalog, base_result.default_source_version)
    for item in base_result.analyses:
        if item.ticker not in catalog_index:
            try:
                ensured = ensure_catalog_entry(paths, item.ticker, base_result.default_source_version)
            except Exception:  # noqa: BLE001
                ensured = None
            if ensured is not None:
                catalog_index[item.ticker] = ensured
    memory_rules = load_memory_rules(paths)
    enriched_result = apply_catalog_and_memory(base_result, catalog_index, memory_rules)
    notebook_json = json.loads(Path(notebook_path).read_text(encoding="utf-8"))
    llm = llm_client or DisabledLLMClient()
    proposals = generate_semantic_proposals(enriched_result, notebook_json, catalog_index, memory_rules, llm)
    written = persist_proposals(paths, proposals)
    return InferenceArtifacts(analysis_result=enriched_result, proposals=written)


def generate_semantic_proposals(
    result: NotebookAnalysisResult,
    notebook_json: dict[str, Any],
    catalog_index: dict[str, Record],
    memory_rules: dict[str, Record],
    llm_client: LLMClient,
) -> list[Record]:
    proposals: list[Record] = []
    sources = extract_cell_texts(notebook_json)
    for item in result.analyses:
        matched_rules = find_matching_memory_rules(memory_rules.values(), item.ticker, result.spec_slug, "series")
        catalog_record = catalog_index.get(item.ticker)
        evidence = build_series_evidence(item, result, catalog_record, matched_rules, sources)
        proposal = build_series_proposal(item, result, catalog_record, matched_rules, evidence)
        if llm_client.is_enabled() and (proposal["confidence"] < 0.9 or item.official_series_name == UNRESOLVED):
            proposal = merge_llm_inference(proposal, evidence, llm_client)
        proposals.append(proposal)
    return proposals


def extract_cell_texts(notebook_json: dict[str, Any]) -> list[str]:
    values: list[str] = []
    for cell in notebook_json.get("cells", []):
        source = cell.get("source", [])
        if isinstance(source, list):
            values.append("".join(source))
        else:
            values.append(str(source))
    return values


def collect_ticker_snippets(sources: list[str], ticker: str, limit: int = 5) -> list[str]:
    normalized = ticker.replace(".", "_")
    snippets: list[str] = []
    for text in sources:
        if ticker not in text and normalized not in text:
            continue
        for line in text.splitlines():
            if ticker in line or normalized in line:
                snippets.append(line.strip())
                if len(snippets) >= limit:
                    return snippets
    return snippets


def collect_indicator_hints(item: TickerAnalysis, result: NotebookAnalysisResult) -> list[str]:
    hints: list[str] = []
    for indicator in result.indicators:
        if f"evds:{item.ticker}" not in indicator.input_ids:
            continue
        if indicator.formula_expression:
            hints.append(f"{indicator.id}: {indicator.formula_expression}")
        elif indicator.formula_description:
            hints.append(f"{indicator.id}: {indicator.formula_description}")
    return hints[:5]


def build_series_evidence(
    item: TickerAnalysis,
    result: NotebookAnalysisResult,
    catalog_record: Record | None,
    matched_rules: list[Record],
    sources: list[str],
) -> dict[str, Any]:
    return {
        "ticker": item.ticker,
        "notebook_slug": result.spec_slug,
        "official_series_name": item.official_series_name,
        "context_title": item.context_title,
        "frequency": item.frequency,
        "unit": item.unit,
        "role": item.notebook_role,
        "status": item.notebook_status,
        "theme_ids": list(item.linked_theme_ids),
        "indicator_ids": list(item.linked_indicator_ids),
        "source_dependency_ids": list(item.linked_source_dependency_ids),
        "catalog_record": {
            "id": catalog_record.get("id"),
            "title": catalog_record.get("title"),
            "frequency": catalog_record.get("frequency"),
            "unit": catalog_record.get("unit"),
            "data_group": catalog_record.get("data_group"),
            "category": catalog_record.get("category"),
        }
        if catalog_record
        else {},
        "memory_rules": [
            {
                "id": rule["id"],
                "scope": rule.get("scope"),
                "match_pattern": rule.get("match_pattern"),
                "resolved_title": rule.get("resolved_title"),
                "resolved_unit": rule.get("resolved_unit"),
                "resolved_frequency": rule.get("resolved_frequency"),
            }
            for rule in matched_rules
        ],
        "source_snippets": collect_ticker_snippets(sources, item.ticker),
        "indicator_hints": collect_indicator_hints(item, result),
        "notes": item.notes,
    }


def build_series_proposal(
    item: TickerAnalysis,
    result: NotebookAnalysisResult,
    catalog_record: Record | None,
    matched_rules: list[Record],
    evidence: dict[str, Any],
) -> Record:
    candidate_title = best_title(item, catalog_record)
    candidate_unit = str(catalog_record.get("unit") or "") if catalog_record and catalog_record.get("unit") not in {"", "unknown"} else item.unit
    candidate_frequency = str(catalog_record.get("frequency") or "") if catalog_record and catalog_record.get("frequency") not in {"", "unknown"} else item.frequency
    confidence = score_series_confidence(item, catalog_record, matched_rules, evidence)
    status = "review_pending" if candidate_title and candidate_frequency else "unresolved"
    proposal_id = build_proposal_id(result.spec_slug, "series", item.ticker, evidence)
    formula_hint = evidence["indicator_hints"][0] if evidence["indicator_hints"] else ""
    return normalize_proposal_input(
        {
            "id": proposal_id,
            "title": f"Semantic proposal for {item.ticker}",
            "target_type": "series",
            "target_id": f"evds:{item.ticker}",
            "ticker": item.ticker,
            "notebook_slug": result.spec_slug,
            "notebook_path": str(result.notebook_path),
            "candidate_title": candidate_title,
            "candidate_unit": candidate_unit,
            "candidate_frequency": candidate_frequency,
            "candidate_role": item.notebook_role,
            "candidate_theme_ids": list(item.linked_theme_ids),
            "candidate_indicator_inputs": list(item.linked_indicator_ids),
            "candidate_formula_hint": formula_hint,
            "confidence": round(confidence, 2),
            "status": status,
            "source": "heuristic",
            "evidence_fingerprint": build_evidence_fingerprint(evidence),
            "catalog_record_id": str(catalog_record.get("id") or "") if catalog_record else "",
            "memory_rule_ids": [rule["id"] for rule in matched_rules],
            "evidence": evidence,
            "notes": build_proposal_note(item, catalog_record),
        }
    )


def best_title(item: TickerAnalysis, catalog_record: Record | None) -> str:
    if catalog_record and catalog_record.get("title") not in {"", "unknown", None}:
        return str(catalog_record.get("title"))
    if item.official_series_name not in {"", UNRESOLVED}:
        return item.official_series_name
    if item.context_title:
        return item.context_title
    if item.notebook_label:
        return item.notebook_label
    return item.ticker


def score_series_confidence(
    item: TickerAnalysis,
    catalog_record: Record | None,
    matched_rules: list[Record],
    evidence: dict[str, Any],
) -> float:
    score = 0.15
    if item.official_series_name not in {"", UNRESOLVED}:
        score += 0.2
    if catalog_record:
        score += 0.25
        if catalog_record.get("unit") not in {"", "unknown", None}:
            score += 0.1
        if catalog_record.get("frequency") not in {"", "unknown", None}:
            score += 0.1
    if evidence.get("source_snippets"):
        score += 0.1
    if evidence.get("indicator_hints"):
        score += 0.05
    if matched_rules:
        score += 0.15
    return min(score, 0.99)


def canonical_series_title_from_proposal(proposal: Record) -> str:
    evidence = proposal.get("evidence") or {}
    if isinstance(evidence, dict):
        catalog_record = evidence.get("catalog_record") or {}
        if isinstance(catalog_record, dict):
            catalog_title = str(catalog_record.get("title") or "").strip()
            if catalog_title:
                return catalog_title
    candidate_title = str(proposal.get("candidate_title") or "").strip()
    if candidate_title:
        return candidate_title
    return str(proposal.get("ticker") or proposal.get("target_id") or "").strip()


def build_proposal_note(item: TickerAnalysis, catalog_record: Record | None) -> str:
    parts: list[str] = []
    if catalog_record:
        parts.append(f"Catalog source: {catalog_record['id']}")
    if item.notes:
        parts.append(item.notes)
    return " | ".join(parts)


def build_proposal_id(notebook_slug: str, target_type: str, target_key: str, evidence: dict[str, Any]) -> str:
    digest = build_evidence_fingerprint(evidence)[:12]
    return f"proposal:{notebook_slug}:{target_type}:{target_key.replace('.', '_')}:{digest}"


def build_evidence_fingerprint(evidence: dict[str, Any]) -> str:
    payload = json.dumps(evidence, sort_keys=True, ensure_ascii=True)
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()


def merge_llm_inference(proposal: Record, evidence: dict[str, Any], llm_client: LLMClient) -> Record:
    prompt = compose_llm_prompt(proposal, evidence)
    schema = {
        "type": "object",
        "properties": {
            "candidate_title": {"type": "string"},
            "candidate_unit": {"type": "string"},
            "candidate_frequency": {"type": "string"},
            "candidate_role": {"type": "string"},
            "candidate_theme_ids": {"type": "array", "items": {"type": "string"}},
            "candidate_indicator_inputs": {"type": "array", "items": {"type": "string"}},
            "candidate_formula_hint": {"type": "string"},
            "confidence": {"type": "number"},
            "notes": {"type": "string"},
        },
        "required": ["confidence"],
    }
    llm_output = llm_client.generate_structured(prompt, schema)
    if not llm_output:
        return proposal
    merged = dict(proposal)
    for key in (
        "candidate_title",
        "candidate_unit",
        "candidate_frequency",
        "candidate_role",
        "candidate_formula_hint",
    ):
        value = llm_output.get(key)
        if isinstance(value, str) and value.strip():
            merged[key] = value.strip()
    for key in ("candidate_theme_ids", "candidate_indicator_inputs"):
        value = llm_output.get(key)
        if isinstance(value, list):
            merged[key] = [str(item).strip() for item in value if str(item).strip()]
    confidence = llm_output.get("confidence")
    if isinstance(confidence, (int, float)):
        merged["confidence"] = round(max(float(confidence), float(proposal["confidence"])), 2)
    notes = llm_output.get("notes")
    if isinstance(notes, str) and notes.strip():
        merged["notes"] = " | ".join(part for part in (proposal.get("notes"), notes.strip()) if part)
    merged["source"] = "hybrid"
    merged["llm_provider"] = llm_client.provider_name
    merged["llm_model"] = llm_client.model_name
    return normalize_proposal_input(merged)


def compose_llm_prompt(proposal: Record, evidence: dict[str, Any]) -> str:
    return json.dumps(
        {
            "instruction": "Infer semantic metadata using only the evidence. Leave unknown fields empty if not supported.",
            "proposal": {
                "target_type": proposal["target_type"],
                "target_id": proposal["target_id"],
                "candidate_title": proposal["candidate_title"],
                "candidate_unit": proposal["candidate_unit"],
                "candidate_frequency": proposal["candidate_frequency"],
                "candidate_role": proposal["candidate_role"],
                "candidate_theme_ids": proposal["candidate_theme_ids"],
                "candidate_indicator_inputs": proposal["candidate_indicator_inputs"],
                "candidate_formula_hint": proposal["candidate_formula_hint"],
            },
            "evidence": evidence,
        },
        ensure_ascii=False,
        indent=2,
    )


def persist_proposals(paths: RegistryPaths, proposals: list[Record]) -> list[Record]:
    existing = load_proposals(paths)
    written: list[Record] = []
    for proposal in proposals:
        current = existing.get(proposal["id"])
        if current and current.get("status") in {"rejected", "approved", "manual_review"} and current.get("evidence_fingerprint") == proposal.get("evidence_fingerprint"):
            proposal["status"] = current["status"]
            proposal["promoted_record_id"] = current.get("promoted_record_id") or ""
            proposal["promoted_memory_rule_id"] = current.get("promoted_memory_rule_id") or ""
            proposal["approval_mode"] = current.get("approval_mode") or ""
            proposal["approval_reason"] = current.get("approval_reason") or ""
        write_record(paths.proposals, proposal)
        written.append(proposal)
    return written


def write_inference_report(artifacts: InferenceArtifacts, output_path: str | Path) -> Path:
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    catalog_rows = "\n".join(
        f"| `{proposal.get('ticker')}` | `{proposal.get('catalog_record_id') or '-'}` | {proposal.get('candidate_title') or '-'} | {proposal.get('candidate_frequency') or '-'} | {proposal.get('candidate_unit') or '-'} |"
        for proposal in artifacts.proposals
    )
    proposal_rows = "\n".join(
        f"| `{proposal['id']}` | `{proposal['target_id']}` | {proposal.get('candidate_title') or '-'} | {proposal.get('confidence')} | {proposal.get('status')} | {proposal.get('source')} |"
        for proposal in sorted(artifacts.proposals, key=lambda item: (-float(item.get("confidence") or 0.0), item["id"]))
    )
    content = "\n".join(
        [
            "# Semantic Inference Summary",
            "",
            f"- Notebook: `{artifacts.analysis_result.notebook_path.name}`",
            f"- Spec: `{artifacts.analysis_result.spec_slug}`",
            f"- Proposal count: `{len(artifacts.proposals)}`",
            f"- Unresolved ticker after enrichment: `{len(artifacts.analysis_result.unresolved_items)}`",
            "",
            "## Catalog Evidence",
            "",
            "| Ticker | Catalog ID | Candidate Title | Frequency | Unit |",
            "| --- | --- | --- | --- | --- |",
            catalog_rows or "| - | - | - | - | - |",
            "",
            "## Proposal Status",
            "",
            "| Proposal ID | Target | Candidate Title | Confidence | Status | Source |",
            "| --- | --- | --- | --- | --- | --- |",
            proposal_rows or "| - | - | - | - | - | - |",
            "",
            "## Belirsizlikler",
            "",
            *([f"- `{ticker}`" for ticker in artifacts.analysis_result.unresolved_items] or ["-"]),
            "",
        ]
    )
    output_file.write_text(content, encoding="utf-8")
    return output_file


def write_proposals_json(proposals: list[Record], output_path: str | Path) -> Path:
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps(proposals, ensure_ascii=False, indent=2), encoding="utf-8")
    return output_file


def write_candidate_drafts_csv(proposals: list[Record], output_path: str | Path) -> Path:
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "record_type",
        "id",
        "title",
        "ticker",
        "source_version",
        "frequency",
        "unit",
        "description",
        "usage",
        "theme_ids",
    ]
    with output_file.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for proposal in proposals:
            if proposal.get("target_type") != "series" or proposal.get("status") == "rejected":
                continue
            ticker = proposal.get("ticker") or proposal["target_id"].split(":", 1)[-1]
            writer.writerow(
                {
                    "record_type": "series",
                    "id": proposal["target_id"],
                    "title": proposal.get("candidate_title") or ticker,
                    "ticker": ticker,
                    "source_version": infer_source_version_from_catalog_record_id(proposal.get("catalog_record_id") or ""),
                    "frequency": proposal.get("candidate_frequency") or "",
                    "unit": proposal.get("candidate_unit") or "",
                    "description": compose_series_description_from_proposal(proposal),
                    "usage": f"Inferred notebook role: {proposal.get('candidate_role') or '-'}",
                    "theme_ids": "|".join(split_list(proposal.get("candidate_theme_ids"))),
                }
            )
    return output_file


def compose_series_description_from_proposal(proposal: Record) -> str:
    parts = [
        f"Semantic proposal for {proposal['target_id']}",
        f"Confidence: {proposal.get('confidence')}",
    ]
    official_title = canonical_series_title_from_proposal(proposal)
    if official_title:
        parts.append(f"EVDS resmi seri adi: {official_title}")
    evidence = proposal.get("evidence") or {}
    if isinstance(evidence, dict):
        context_title = str(evidence.get("context_title") or "").strip()
        if context_title and context_title != official_title:
            parts.append(f"Notebook baglami: {context_title}")
        notebook_label = str(evidence.get("official_series_name") or "").strip()
        if notebook_label and notebook_label not in {"", UNRESOLVED, official_title, context_title}:
            parts.append(f"Notebook cikarimi: {notebook_label}")
    if proposal.get("notes"):
        parts.append(str(proposal["notes"]))
    return " | ".join(parts)


def infer_source_version_from_catalog_record_id(record_id: str) -> str:
    parts = record_id.split(":", 2)
    if len(parts) >= 3:
        return parts[1]
    return ""


def review_proposals(
    paths: RegistryPaths,
    *,
    status: str = "",
    notebook_slug: str = "",
    target_type: str = "",
    min_confidence: float = 0.0,
) -> list[Record]:
    proposals = load_proposals(paths).values()
    filtered: list[Record] = []
    for proposal in proposals:
        if status and proposal.get("status") != status:
            continue
        if notebook_slug and proposal.get("notebook_slug") != notebook_slug:
            continue
        if target_type and proposal.get("target_type") != target_type:
            continue
        if float(proposal.get("confidence") or 0.0) < min_confidence:
            continue
        filtered.append(proposal)
    return sorted(filtered, key=lambda item: (-float(item.get("confidence") or 0.0), item["id"]))


def auto_approve_proposals(
    paths: RegistryPaths,
    llm_client: LLMClient,
    *,
    notebook_slug: str = "",
    target_type: str = "",
    min_confidence: float = 0.9,
    limit: int = 0,
) -> AutoApproveSummary:
    candidates = review_proposals(paths, status="review_pending", notebook_slug=notebook_slug, min_confidence=0.0)
    if target_type:
        candidates = [p for p in candidates if p.get("target_type") == target_type]
    needs_llm = any(str(p.get("target_type") or "series") == "series" for p in candidates)
    if needs_llm and (llm_client is None or not llm_client.is_enabled()):
        raise ValueError("LLM client must be enabled for auto-approve of series proposals.")
    if limit > 0:
        candidates = candidates[:limit]
    proposal_index = build_series_proposal_index(load_proposals(paths).values())
    approved_registry = load_registry(paths)
    memory_rules = load_memory_rules(paths)
    summary = AutoApproveSummary()

    for proposal in candidates:
        proposal_target_type = str(proposal.get("target_type") or "series")
        manual_reason = assess_auto_approval_risk(
            proposal,
            proposal_index=proposal_index,
            approved_registry=approved_registry,
            memory_rules=memory_rules,
            min_confidence=min_confidence,
        )
        if manual_reason:
            mark_proposal_manual_review(paths, proposal, manual_reason)
            summary.manual_review += 1
            continue

        if proposal_target_type == "series":
            decision, reason = request_llm_auto_approval_decision(
                proposal,
                llm_client=llm_client,
                proposal_index=proposal_index,
                approved_registry=approved_registry,
                memory_rules=memory_rules,
            )
            if decision != "approve":
                mark_proposal_manual_review(paths, proposal, reason)
                summary.manual_review += 1
                continue
            approval_mode = "auto_llm"
        else:
            reason = "Implied proposal passed deterministic safety checks."
            approval_mode = "auto_heuristic"

        _, _, updated_proposal = apply_proposal_approval(
            paths,
            proposal,
            destination="canonical",
            approval_mode=approval_mode,
            approval_reason=reason,
        )
        if proposal_target_type == "series":
            proposal_index = update_series_proposal_index(proposal_index, updated_proposal)
        approved_registry = load_registry(paths)
        memory_rules = load_memory_rules(paths)
        summary.approved += 1
    return summary


def _score_implied_confidence(
    target_type: str,
    *,
    ref_count: int,
    has_formula: bool = False,
) -> float:
    base = min(0.5 + ref_count * 0.1, 0.85)  # 1 ref→0.60, 3 ref→0.80, 5+→0.85
    if has_formula:
        base = min(base + 0.10, 0.90)
    return round(base, 2)


def generate_implied_proposals(
    paths: RegistryPaths,
    *,
    target_types: list[str] | None = None,
) -> ImpliedProposalSummary:
    """Generate review_pending proposals for theme/indicator IDs referenced in approved proposals but lacking records."""
    if target_types is None:
        target_types = ["indicator", "theme"]

    registry = load_registry(paths)
    all_proposals = load_proposals(paths)
    existing_proposal_targets = {p["target_id"] for p in all_proposals.values()}

    theme_refs: dict[str, set[str]] = {}
    indicator_refs: dict[str, dict[str, Any]] = {}

    for proposal in all_proposals.values():
        if proposal.get("status") not in ("approved", "review_pending"):
            continue
        nb = str(proposal.get("notebook_slug") or "")

        for theme_id in split_list(proposal.get("candidate_theme_ids")):
            theme_refs.setdefault(theme_id, set()).add(nb)

        formula_block = str(proposal.get("candidate_formula_hint") or "")
        for ind_id in split_list(proposal.get("candidate_indicator_inputs")):
            entry = indicator_refs.setdefault(ind_id, {"formula_hints": [], "input_ids": [], "notebooks": set()})
            entry["notebooks"].add(nb)
            for line in formula_block.splitlines():
                stripped = line.strip()
                if stripped.startswith(ind_id + ":") and stripped not in entry["formula_hints"]:
                    entry["formula_hints"].append(stripped)
                    formula_part = stripped[len(ind_id) + 1:].strip()
                    entry["input_ids"].extend(re.findall(r"evds:[A-Za-z0-9_.]+", formula_part))

    summary = ImpliedProposalSummary()

    if "theme" in target_types:
        for theme_id, notebooks in theme_refs.items():
            if theme_id in registry or theme_id in existing_proposal_targets:
                summary.skipped_existing += 1
                continue
            slug = theme_id.split(":", 1)[-1]
            title = " ".join(w.capitalize() for w in slug.replace("-", " ").split())
            confidence = _score_implied_confidence("theme", ref_count=len(notebooks))
            proposal = normalize_proposal_input({
                "target_id": theme_id,
                "target_type": "theme",
                "title": f"Implied theme proposal for {theme_id}",
                "candidate_title": title,
                "confidence": confidence,
                "source": "heuristic",
                "notes": f"Implied from {len(notebooks)} notebook(s): {', '.join(sorted(notebooks))}",
            })
            write_record(paths.proposals, proposal)
            existing_proposal_targets.add(theme_id)
            summary.created += 1

    if "indicator" in target_types:
        for ind_id, data in indicator_refs.items():
            if ind_id in registry or ind_id in existing_proposal_targets:
                summary.skipped_existing += 1
                continue
            slug = ind_id.split(":", 1)[-1]
            title = " ".join(w.capitalize() for w in slug.replace("-", " ").split())
            input_ids = list(dict.fromkeys(data["input_ids"]))
            formula_hint = "\n".join(data["formula_hints"])
            confidence = _score_implied_confidence(
                "indicator",
                ref_count=len(data["notebooks"]),
                has_formula=bool(data["formula_hints"]),
            )
            proposal = normalize_proposal_input({
                "target_id": ind_id,
                "target_type": "indicator",
                "title": f"Implied indicator proposal for {ind_id}",
                "candidate_title": title,
                "candidate_formula_hint": formula_hint,
                "candidate_indicator_inputs": input_ids,
                "confidence": confidence,
                "source": "heuristic",
                "notes": f"Implied from {len(data['notebooks'])} notebook(s): {', '.join(sorted(data['notebooks']))}",
            })
            write_record(paths.proposals, proposal)
            existing_proposal_targets.add(ind_id)
            summary.created += 1

    return summary


@dataclass(slots=True)
class BackfillSummary:
    themes_updated: int = 0
    source_deps_updated: int = 0


@dataclass(slots=True)
class EnrichIndicatorSummary:
    enriched: int = 0
    skipped: int = 0


def enrich_indicator_proposals_from_specs(paths: RegistryPaths) -> EnrichIndicatorSummary:
    """Update manual_review indicator proposals with input_ids from NotebookSpec templates."""
    from .notebook_analysis import ALL_SPECS
    spec_indicators = {}
    for spec in ALL_SPECS:
        for ind in spec.indicators:
            spec_indicators[ind.id] = ind
    all_proposals = load_proposals(paths)
    summary = EnrichIndicatorSummary()
    for proposal in all_proposals.values():
        if proposal.get("status") != "manual_review":
            continue
        if proposal.get("target_type") != "indicator":
            continue
        target_id = str(proposal.get("target_id") or "")
        template = spec_indicators.get(target_id)
        if template is None:
            summary.skipped += 1
            continue
        updated = dict(proposal)
        updated["candidate_indicator_inputs"] = list(template.input_ids)
        updated["candidate_formula_hint"] = template.formula_expression or template.formula_description
        updated["status"] = "review_pending"
        updated["approval_reason"] = ""
        if template.theme_ids:
            updated["candidate_theme_ids"] = list(template.theme_ids)
        write_record(paths.proposals, updated)
        summary.enriched += 1
    return summary


def backfill_cross_references(paths: RegistryPaths) -> BackfillSummary:
    """Scan approved proposals to populate theme↔source_dep linkage on registry records."""
    all_proposals = load_proposals(paths)
    registry = load_registry(paths)

    theme_to_source_deps: dict[str, set[str]] = {}
    source_dep_to_themes: dict[str, set[str]] = {}

    for proposal in all_proposals.values():
        if proposal.get("status") != "approved":
            continue
        theme_ids = split_list(proposal.get("candidate_theme_ids"))
        evidence = proposal.get("evidence") or {}
        src_dep_ids = split_list(evidence.get("source_dependency_ids"))
        if not theme_ids or not src_dep_ids:
            continue
        for tid in theme_ids:
            theme_to_source_deps.setdefault(tid, set()).update(src_dep_ids)
        for sid in src_dep_ids:
            source_dep_to_themes.setdefault(sid, set()).update(theme_ids)

    summary = BackfillSummary()

    for theme_id, src_ids in theme_to_source_deps.items():
        record = registry.get(theme_id)
        if not record or record["record_type"] != "theme":
            continue
        existing = set(split_list(record.get("source_dependency_ids")))
        new_ids = src_ids - existing
        if not new_ids:
            continue
        record["source_dependency_ids"] = sorted(existing | new_ids)
        write_record(paths.canonical_dir(record["record_type"]), record)
        summary.themes_updated += 1

    for src_id, t_ids in source_dep_to_themes.items():
        record = registry.get(src_id)
        if not record or record["record_type"] != "source_dependency":
            continue
        existing = set(split_list(record.get("theme_ids")))
        new_ids = t_ids - existing
        if not new_ids:
            continue
        record["theme_ids"] = sorted(existing | new_ids)
        write_record(paths.canonical_dir(record["record_type"]), record)
        summary.source_deps_updated += 1

    return summary


def promote_proposal(paths: RegistryPaths, proposal_id: str) -> tuple[Record | None, Record]:
    proposal = load_record(paths.proposals, proposal_id)
    if proposal is None:
        raise ValueError(f"Proposal not found: {proposal_id}")
    draft_record, memory_rule, _ = apply_proposal_approval(
        paths,
        proposal,
        destination="draft",
        approval_mode="manual",
        approval_reason="Manual proposal promote.",
    )
    return draft_record, memory_rule


def reject_proposal(paths: RegistryPaths, proposal_id: str) -> Record:
    proposal = load_record(paths.proposals, proposal_id)
    if proposal is None:
        raise ValueError(f"Proposal not found: {proposal_id}")
    proposal["status"] = "rejected"
    proposal["approval_reason"] = proposal.get("approval_reason") or "Rejected manually."
    write_record(paths.proposals, proposal)
    return proposal


def build_record_from_proposal(proposal: Record) -> Record | None:
    target_type = proposal.get("target_type")
    if target_type == "series":
        ticker = proposal.get("ticker") or proposal["target_id"].split(":", 1)[-1]
        return normalize_series_input(
            {
                "id": proposal["target_id"],
                "ticker": ticker,
                "title": canonical_series_title_from_proposal(proposal) or ticker,
                "source_version": infer_source_version_from_catalog_record_id(proposal.get("catalog_record_id") or ""),
                "frequency": proposal.get("candidate_frequency") or "",
                "unit": proposal.get("candidate_unit") or "",
                "description": compose_series_description_from_proposal(proposal),
                "usage": f"Inferred notebook role: {proposal.get('candidate_role') or '-'}",
                "theme_ids": proposal.get("candidate_theme_ids") or [],
            }
        )
    if target_type == "indicator":
        return normalize_indicator_input(
            {
                "id": proposal["target_id"],
                "title": proposal.get("candidate_title") or proposal["target_id"],
                "input_ids": proposal.get("candidate_indicator_inputs") or [],
                "formula_description": proposal.get("candidate_formula_hint") or "Inferred from semantic proposal.",
            }
        )
    if target_type == "theme":
        return normalize_theme_input(
            {
                "id": proposal["target_id"],
                "title": proposal.get("candidate_title") or proposal["target_id"],
                "description": proposal.get("notes") or "Inferred from semantic proposal.",
                "indicator_ids": proposal.get("candidate_indicator_inputs") or [],
            }
        )
    return None


def build_memory_rule_from_proposal(proposal: Record) -> Record:
    ticker = proposal.get("ticker") or proposal["target_id"].split(":", 1)[-1]
    target_type = proposal.get("target_type") or "series"
    resolved_role = proposal.get("candidate_role") or ""
    resolved_title = proposal.get("candidate_title") or ""
    if target_type == "series":
        resolved_title = canonical_series_title_from_proposal(proposal)
        resolved_role = ""
    return normalize_memory_rule_input(
        {
            "title": f"Memory rule for {ticker}",
            "scope": "global",
            "match_pattern": ticker,
            "target_type": target_type,
            "notebook_slug": proposal.get("notebook_slug") or "",
            "resolved_title": resolved_title,
            "resolved_unit": proposal.get("candidate_unit") or "",
            "resolved_frequency": proposal.get("candidate_frequency") or "",
            "resolved_role": resolved_role,
            "resolved_theme_ids": proposal.get("candidate_theme_ids") or [],
            "resolved_formula_hint": proposal.get("candidate_formula_hint") or "",
            "evidence_source": f"proposal:{proposal['id']}",
            "approved_by": getpass.getuser(),
            "approved_at": datetime.now(timezone.utc).isoformat(),
            "notes": proposal.get("notes") or "",
        }
    )


def apply_proposal_approval(
    paths: RegistryPaths,
    proposal: Record,
    *,
    destination: str,
    approval_mode: str,
    approval_reason: str,
) -> tuple[Record | None, Record, Record]:
    materialized_record = build_record_from_proposal(proposal)
    if materialized_record is not None:
        if destination == "draft":
            write_record(paths.drafts, materialized_record)
        elif destination == "canonical":
            approved_record = dict(materialized_record)
            approved_record["status"] = "approved"
            validate_record(approved_record, load_registry(paths))
            write_record(paths.canonical_dir(approved_record["record_type"]), approved_record)
            delete_record(paths.drafts, approved_record["id"])
            materialized_record = approved_record
        else:
            raise ValueError(f"Unknown proposal approval destination: {destination}")
    memory_rule = build_memory_rule_from_proposal(proposal)
    write_record(paths.memory, memory_rule)
    updated_proposal = dict(proposal)
    updated_proposal["status"] = "approved"
    updated_proposal["promoted_record_id"] = materialized_record["id"] if materialized_record else ""
    updated_proposal["promoted_memory_rule_id"] = memory_rule["id"]
    updated_proposal["approval_mode"] = approval_mode
    updated_proposal["approval_reason"] = approval_reason
    write_record(paths.proposals, updated_proposal)
    return materialized_record, memory_rule, updated_proposal


def mark_proposal_manual_review(paths: RegistryPaths, proposal: Record, reason: str) -> Record:
    updated = dict(proposal)
    updated["status"] = "manual_review"
    updated["approval_reason"] = reason
    write_record(paths.proposals, updated)
    return updated


def build_series_proposal_index(proposals: Any) -> dict[str, list[Record]]:
    index: dict[str, list[Record]] = {}
    for proposal in proposals:
        if proposal.get("target_type") != "series" or proposal.get("status") == "rejected":
            continue
        ticker = str(proposal.get("ticker") or proposal.get("target_id", "").split(":", 1)[-1]).strip()
        if not ticker:
            continue
        index.setdefault(ticker, []).append(proposal)
    return index


def update_series_proposal_index(index: dict[str, list[Record]], updated_proposal: Record) -> dict[str, list[Record]]:
    ticker = str(updated_proposal.get("ticker") or updated_proposal.get("target_id", "").split(":", 1)[-1]).strip()
    if not ticker:
        return index
    current = [proposal for proposal in index.get(ticker, []) if proposal["id"] != updated_proposal["id"]]
    current.append(updated_proposal)
    index[ticker] = current
    return index


def assess_auto_approval_risk(
    proposal: Record,
    *,
    proposal_index: dict[str, list[Record]],
    approved_registry: dict[str, Record],
    memory_rules: dict[str, Record],
    min_confidence: float,
) -> str:
    reasons: list[str] = []
    if proposal.get("status") != "review_pending":
        reasons.append(f"Proposal status is {proposal.get('status') or '-'} instead of review_pending.")
    if proposal.get("source") != "heuristic":
        reasons.append(f"Proposal source is {proposal.get('source') or '-'}; heuristic-only auto-approve is required.")
    if float(proposal.get("confidence") or 0.0) < min_confidence:
        reasons.append(f"Confidence {proposal.get('confidence')} is below the auto-approve threshold {min_confidence}.")

    target_type = str(proposal.get("target_type") or "series")
    if target_type == "series":
        missing = []
        for field_name, label in (
            ("candidate_title", "candidate_title"),
            ("candidate_unit", "candidate_unit"),
            ("candidate_frequency", "candidate_frequency"),
            ("candidate_role", "candidate_role"),
        ):
            if not str(proposal.get(field_name) or "").strip():
                missing.append(label)
        if missing:
            reasons.append(f"Missing required series fields: {', '.join(missing)}.")
        title_unit_conflict = detect_title_unit_conflict(proposal)
        if title_unit_conflict:
            reasons.append(title_unit_conflict)
        reasons.extend(find_conflicting_proposals_for_ticker(proposal, proposal_index))
        reasons.extend(find_existing_registry_conflicts(proposal, approved_registry, memory_rules))
    elif target_type == "indicator":
        if not str(proposal.get("candidate_title") or "").strip():
            reasons.append("Missing required field: candidate_title.")
        if not split_list(proposal.get("candidate_indicator_inputs")):
            reasons.append("Indicator has no input_ids; manual review required to define formula inputs.")
    else:
        if not str(proposal.get("candidate_title") or "").strip():
            reasons.append("Missing required field: candidate_title.")

    return " ".join(reasons).strip()


def find_conflicting_proposals_for_ticker(proposal: Record, proposal_index: dict[str, list[Record]]) -> list[str]:
    ticker = str(proposal.get("ticker") or proposal.get("target_id", "").split(":", 1)[-1]).strip()
    if not ticker:
        return ["Ticker is missing from proposal."]
    conflicts: list[str] = []
    current_signature = proposal_signature(proposal)
    for sibling in proposal_index.get(ticker, []):
        if sibling["id"] == proposal["id"] or sibling.get("status") == "rejected":
            continue
        if proposal_signature(sibling) != current_signature:
            conflicts.append(
                f"Ticker {ticker} has conflicting proposal values across notebooks ({proposal.get('notebook_slug') or '-'} vs {sibling.get('notebook_slug') or '-' })."
            )
            break
    return conflicts


def find_existing_registry_conflicts(
    proposal: Record,
    approved_registry: dict[str, Record],
    memory_rules: dict[str, Record],
) -> list[str]:
    conflicts: list[str] = []
    target = approved_registry.get(str(proposal.get("target_id") or ""))
    if target and target.get("record_type") == "series":
        for proposal_field, record_field in (
            ("candidate_title", "title"),
            ("candidate_unit", "unit"),
            ("candidate_frequency", "frequency"),
        ):
            if proposal_field == "candidate_title":
                candidate = canonical_series_title_from_proposal(proposal)
            else:
                candidate = str(proposal.get(proposal_field) or "").strip()
            existing = str(target.get(record_field) or "").strip()
            if candidate and existing and not semantic_values_match(record_field, candidate, existing):
                conflicts.append(
                    f"Approved series {target['id']} already has {record_field}={existing}, proposal suggests {candidate}."
                )
    ticker = str(proposal.get("ticker") or proposal.get("target_id", "").split(":", 1)[-1]).strip()
    matched_rules = find_matching_memory_rules(
        list(memory_rules.values()),
        ticker,
        str(proposal.get("notebook_slug") or ""),
        str(proposal.get("target_type") or "series"),
    )
    for rule in matched_rules:
        if str(rule.get("scope") or "global") == "notebook_slug":
            conflicts.append(f"Notebook-specific memory rule exists for {ticker}: {rule['id']}.")
            continue
        for proposal_field, rule_field in (
            ("candidate_title", "resolved_title"),
            ("candidate_unit", "resolved_unit"),
            ("candidate_frequency", "resolved_frequency"),
        ):
            if proposal_field == "candidate_title":
                candidate = canonical_series_title_from_proposal(proposal)
            else:
                candidate = str(proposal.get(proposal_field) or "").strip()
            existing = str(rule.get(rule_field) or "").strip()
            if candidate and existing and not semantic_values_match(rule_field, candidate, existing):
                conflicts.append(
                    f"Memory rule {rule['id']} already has {rule_field}={existing}, proposal suggests {candidate}."
                )
                break
    return conflicts


def proposal_signature(proposal: Record) -> tuple[str, ...]:
    target_type = str(proposal.get("target_type") or "series").strip() or "series"
    if target_type == "series":
        return (
            comparable_semantic_value("candidate_title", canonical_series_title_from_proposal(proposal)),
            comparable_semantic_value("candidate_unit", str(proposal.get("candidate_unit") or "").strip()),
            str(proposal.get("candidate_frequency") or "").strip(),
        )
    return (
        str(proposal.get("candidate_title") or "").strip(),
        str(proposal.get("candidate_unit") or "").strip(),
        str(proposal.get("candidate_frequency") or "").strip(),
        str(proposal.get("candidate_role") or "").strip(),
    )


def detect_title_unit_conflict(proposal: Record) -> str:
    title = normalize_text_for_match(str(proposal.get("candidate_title") or ""))
    unit = normalize_text_for_match(str(proposal.get("candidate_unit") or ""))
    if not title or not unit:
        return ""
    if "milyon abd dolari" in title and "abd dolar" not in unit:
        return f"candidate_title ({proposal.get('candidate_title')}) contradicts candidate_unit ({proposal.get('candidate_unit')})."
    if "bin tl" in title and "tl" not in unit:
        return f"candidate_title ({proposal.get('candidate_title')}) contradicts candidate_unit ({proposal.get('candidate_unit')})."
    return ""


def normalize_text_for_match(value: str) -> str:
    lowered = value.casefold()
    replacements = {
        "ı": "i",
        "ğ": "g",
        "ü": "u",
        "ş": "s",
        "ö": "o",
        "ç": "c",
        "â": "a",
        "î": "i",
        "û": "u",
    }
    for source, target in replacements.items():
        lowered = lowered.replace(source, target)
    return " ".join(lowered.split())


def comparable_semantic_value(field_name: str, value: str) -> str:
    if field_name in {"candidate_title", "title", "resolved_title", "candidate_unit", "unit", "resolved_unit"}:
        return normalize_text_for_match(value)
    return str(value or "").strip()


def semantic_values_match(field_name: str, left: str, right: str) -> bool:
    return comparable_semantic_value(field_name, left) == comparable_semantic_value(field_name, right)


def request_llm_auto_approval_decision(
    proposal: Record,
    *,
    llm_client: LLMClient,
    proposal_index: dict[str, list[Record]],
    approved_registry: dict[str, Record],
    memory_rules: dict[str, Record],
) -> tuple[str, str]:
    ticker = str(proposal.get("ticker") or proposal.get("target_id", "").split(":", 1)[-1]).strip()
    prompt = json.dumps(
        {
            "instruction": (
                "Deterministic safety checks already passed for this series proposal. "
                "Your job is only to decide whether there is a subtle reason this proposal should still avoid automatic GLOBAL approval. "
                "Approve by default. Choose manual_review only if you can point to a concrete blocker in the payload. "
                "The absence of approved_series or matching_memory_rules is NOT a blocker. "
                "The fact that source=heuristic is NOT a blocker because heuristic-only gating already passed."
            ),
            "prechecked_guards_passed": True,
            "default_decision": "approve",
            "proposal": {
                "id": proposal["id"],
                "target_id": proposal.get("target_id"),
                "ticker": ticker,
                "notebook_slug": proposal.get("notebook_slug"),
                "candidate_title": proposal.get("candidate_title"),
                "candidate_unit": proposal.get("candidate_unit"),
                "candidate_frequency": proposal.get("candidate_frequency"),
                "candidate_role": proposal.get("candidate_role"),
                "confidence": proposal.get("confidence"),
                "source": proposal.get("source"),
                "notes": proposal.get("notes"),
            },
            "same_ticker_proposals": [
                {
                    "id": sibling["id"],
                    "notebook_slug": sibling.get("notebook_slug"),
                    "status": sibling.get("status"),
                    "signature": list(proposal_signature(sibling)),
                }
                for sibling in proposal_index.get(ticker, [])
                if sibling["id"] != proposal["id"] and sibling.get("status") != "rejected"
            ],
            "approved_series": approved_registry.get(str(proposal.get("target_id") or ""), {}),
            "matching_memory_rules": [
                {
                    "id": rule["id"],
                    "scope": rule.get("scope"),
                    "notebook_slug": rule.get("notebook_slug"),
                    "resolved_title": rule.get("resolved_title"),
                    "resolved_unit": rule.get("resolved_unit"),
                    "resolved_frequency": rule.get("resolved_frequency"),
                    "resolved_role": rule.get("resolved_role"),
                }
                for rule in find_matching_memory_rules(
                    list(memory_rules.values()),
                    ticker,
                    str(proposal.get("notebook_slug") or ""),
                    str(proposal.get("target_type") or "series"),
                )
            ],
            "manual_review_requires_concrete_blocker": [
                "cross-notebook conflict",
                "notebook-specific scoping need",
                "title/unit/frequency/role contradiction",
                "approved registry conflict",
                "memory rule conflict",
            ],
        },
        ensure_ascii=False,
    )
    schema = {
        "type": "object",
        "properties": {
            "decision": {"type": "string", "enum": ["approve", "manual_review"]},
            "reason": {"type": "string"},
        },
        "required": ["decision"],
    }
    output = llm_client.generate_structured(prompt, schema)
    decision = str(output.get("decision") or "").strip().lower().replace("-", "_")
    reason = str(output.get("reason") or "").strip()
    if decision == "approve":
        return "approve", reason or "LLM approved automatic global series promotion."
    if should_soften_manual_review_reason(reason):
        return "approve", "LLM returned no concrete blocker after deterministic safety checks."
    return "manual_review", reason or "LLM requested manual review."


def should_soften_manual_review_reason(reason: str) -> bool:
    normalized = normalize_text_for_match(reason)
    if not normalized:
        return True
    soft_markers = (
        "llm requested manual review",
        "approved_series and matching_memory_rules are empty",
        "approved series and matching memory rules are empty",
        "matching_memory_rules is empty",
        "matching memory rules is empty",
        "source is heuristic",
        "no matching memory rules",
        "approved_series is empty",
        "approved series is empty",
    )
    hard_markers = (
        "conflict",
        "contradict",
        "mismatch",
        "notebook-specific",
        "notebook specific",
        "scope",
        "approved series",
        "memory rule",
        "cross-notebook",
        "cross notebook",
        "frequency differs",
        "unit differs",
        "title differs",
        "role differs",
        "ambiguous",
        "unresolved",
        "manual ledger",
        "missing required",
    )
    if any(marker in normalized for marker in hard_markers):
        return False
    return any(marker in normalized for marker in soft_markers)
