from __future__ import annotations

from copy import deepcopy
import json
from typing import Any


Record = dict[str, Any]


def split_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        raw = value.replace(",", "|")
        return [item.strip() for item in raw.split("|") if item.strip()]
    return [str(value).strip()]


def slugify(value: str) -> str:
    allowed = []
    for char in value.lower().strip():
        if char.isalnum():
            allowed.append(char)
        elif char in {" ", "-", "_", "."}:
            allowed.append("-")
    slug = "".join(allowed).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "unnamed"


def normalize_series_input(payload: dict[str, Any]) -> Record:
    ticker = str(payload.get("ticker", "")).strip()
    if not ticker:
        raise ValueError("Series draft requires a ticker.")
    title = str(payload.get("title") or ticker).strip()
    return {
        "record_type": "series",
        "id": str(payload.get("id") or f"evds:{ticker}").strip(),
        "title": title,
        "status": str(payload.get("status") or "draft").strip() or "draft",
        "source": str(payload.get("source") or "evds").strip(),
        "source_version": str(payload.get("source_version") or "").strip(),
        "ticker": ticker,
        "frequency": str(payload.get("frequency") or "").strip(),
        "unit": str(payload.get("unit") or "").strip(),
        "description": str(payload.get("description") or "").strip(),
        "usage": str(payload.get("usage") or "").strip(),
        "official_url": str(payload.get("official_url") or "").strip(),
        "theme_ids": split_list(payload.get("theme_ids")),
        "indicator_ids": split_list(payload.get("indicator_ids")),
    }


def normalize_indicator_input(payload: dict[str, Any]) -> Record:
    title = str(payload.get("title") or "").strip()
    if not title:
        raise ValueError("Indicator draft requires a title.")
    return {
        "record_type": "indicator",
        "id": str(payload.get("id") or f"derived:{slugify(title)}").strip(),
        "title": title,
        "status": str(payload.get("status") or "draft").strip() or "draft",
        "input_ids": split_list(payload.get("input_ids")),
        "formula_expression": str(payload.get("formula_expression") or "").strip(),
        "formula_description": str(payload.get("formula_description") or "").strip(),
        "output_frequency": str(payload.get("output_frequency") or "").strip(),
        "output_unit": str(payload.get("output_unit") or "").strip(),
        "economic_meaning": str(payload.get("economic_meaning") or "").strip(),
        "validation_note": str(payload.get("validation_note") or "").strip(),
        "theme_ids": split_list(payload.get("theme_ids")),
    }


def normalize_theme_input(payload: dict[str, Any]) -> Record:
    title = str(payload.get("title") or "").strip()
    if not title:
        raise ValueError("Theme draft requires a title.")
    return {
        "record_type": "theme",
        "id": str(payload.get("id") or f"theme:{slugify(title)}").strip(),
        "title": title,
        "status": str(payload.get("status") or "draft").strip() or "draft",
        "description": str(payload.get("description") or "").strip(),
        "series_ids": split_list(payload.get("series_ids")),
        "indicator_ids": split_list(payload.get("indicator_ids")),
        "source_dependency_ids": split_list(payload.get("source_dependency_ids")),
        "questions": split_list(payload.get("questions")),
    }


def normalize_source_dependency_input(payload: dict[str, Any]) -> Record:
    title = str(payload.get("title") or "").strip()
    if not title:
        raise ValueError("Source dependency draft requires a title.")
    return {
        "record_type": "source_dependency",
        "id": str(payload.get("id") or f"source:{slugify(title)}").strip(),
        "title": title,
        "status": str(payload.get("status") or "draft").strip() or "draft",
        "source_kind": str(payload.get("source_kind") or "").strip(),
        "requiredness": str(payload.get("requiredness") or "").strip(),
        "source_uri": str(payload.get("source_uri") or "").strip(),
        "local_hint": str(payload.get("local_hint") or "").strip(),
        "description": str(payload.get("description") or "").strip(),
        "usage": str(payload.get("usage") or "").strip(),
        "theme_ids": split_list(payload.get("theme_ids")),
        "indicator_ids": split_list(payload.get("indicator_ids")),
        "validation_note": str(payload.get("validation_note") or "").strip(),
    }


def normalize_catalog_input(payload: dict[str, Any]) -> Record:
    ticker = str(payload.get("ticker", "")).strip()
    if not ticker:
        raise ValueError("Catalog record requires a ticker.")
    source_version = str(payload.get("source_version") or "").strip() or "evds2"
    title = str(payload.get("title") or ticker).strip()
    return {
        "record_type": "catalog",
        "id": str(payload.get("id") or f"catalog:{source_version}:{ticker}").strip(),
        "title": title,
        "status": str(payload.get("status") or "synced").strip() or "synced",
        "source": str(payload.get("source") or "evds").strip(),
        "source_version": source_version,
        "ticker": ticker,
        "frequency": str(payload.get("frequency") or "").strip(),
        "unit": str(payload.get("unit") or "").strip(),
        "category": str(payload.get("category") or "").strip(),
        "data_group": str(payload.get("data_group") or "").strip(),
        "official_url": str(payload.get("official_url") or "").strip(),
        "raw_metadata": payload.get("raw_metadata") or {},
    }


def normalize_memory_rule_input(payload: dict[str, Any]) -> Record:
    match_pattern = str(payload.get("match_pattern") or "").strip()
    if not match_pattern:
        raise ValueError("Memory rule requires match_pattern.")
    scope = str(payload.get("scope") or "global").strip() or "global"
    return {
        "record_type": "memory_rule",
        "id": str(payload.get("id") or f"memory:{slugify(scope)}-{slugify(match_pattern)}").strip(),
        "title": str(payload.get("title") or f"{scope}::{match_pattern}").strip(),
        "status": str(payload.get("status") or "approved").strip() or "approved",
        "scope": scope,
        "match_pattern": match_pattern,
        "target_type": str(payload.get("target_type") or "series").strip() or "series",
        "notebook_slug": str(payload.get("notebook_slug") or "").strip(),
        "resolved_title": str(payload.get("resolved_title") or "").strip(),
        "resolved_unit": str(payload.get("resolved_unit") or "").strip(),
        "resolved_frequency": str(payload.get("resolved_frequency") or "").strip(),
        "resolved_role": str(payload.get("resolved_role") or "").strip(),
        "resolved_theme_ids": split_list(payload.get("resolved_theme_ids")),
        "resolved_formula_hint": str(payload.get("resolved_formula_hint") or "").strip(),
        "evidence_source": str(payload.get("evidence_source") or "").strip(),
        "approved_by": str(payload.get("approved_by") or "").strip(),
        "approved_at": str(payload.get("approved_at") or "").strip(),
        "notes": str(payload.get("notes") or "").strip(),
    }


def normalize_proposal_input(payload: dict[str, Any]) -> Record:
    target_id = str(payload.get("target_id") or "").strip()
    if not target_id:
        raise ValueError("Proposal requires target_id.")
    target_type = str(payload.get("target_type") or "series").strip() or "series"
    proposal_id = str(payload.get("id") or payload.get("proposal_id") or f"proposal:{target_type}:{slugify(target_id)}").strip()
    return {
        "record_type": "proposal",
        "id": proposal_id,
        "proposal_id": proposal_id,
        "title": str(payload.get("title") or f"Proposal for {target_id}").strip(),
        "status": str(payload.get("status") or "review_pending").strip() or "review_pending",
        "target_type": target_type,
        "target_id": target_id,
        "ticker": str(payload.get("ticker") or "").strip(),
        "notebook_slug": str(payload.get("notebook_slug") or "").strip(),
        "notebook_path": str(payload.get("notebook_path") or "").strip(),
        "candidate_title": str(payload.get("candidate_title") or "").strip(),
        "candidate_unit": str(payload.get("candidate_unit") or "").strip(),
        "candidate_frequency": str(payload.get("candidate_frequency") or "").strip(),
        "candidate_role": str(payload.get("candidate_role") or "").strip(),
        "candidate_theme_ids": split_list(payload.get("candidate_theme_ids")),
        "candidate_indicator_inputs": split_list(payload.get("candidate_indicator_inputs")),
        "candidate_formula_hint": str(payload.get("candidate_formula_hint") or "").strip(),
        "confidence": float(payload.get("confidence") or 0.0),
        "source": str(payload.get("source") or "heuristic").strip() or "heuristic",
        "evidence_fingerprint": str(payload.get("evidence_fingerprint") or "").strip(),
        "catalog_record_id": str(payload.get("catalog_record_id") or "").strip(),
        "memory_rule_ids": split_list(payload.get("memory_rule_ids")),
        "evidence": payload.get("evidence") or {},
        "llm_provider": str(payload.get("llm_provider") or "").strip(),
        "llm_model": str(payload.get("llm_model") or "").strip(),
        "promoted_record_id": str(payload.get("promoted_record_id") or "").strip(),
        "promoted_memory_rule_id": str(payload.get("promoted_memory_rule_id") or "").strip(),
        "approval_mode": str(payload.get("approval_mode") or "").strip(),
        "approval_reason": str(payload.get("approval_reason") or "").strip(),
        "notes": str(payload.get("notes") or "").strip(),
    }


def normalize_import_row(payload: dict[str, Any]) -> Record:
    record_type = str(payload.get("record_type") or "").strip().lower()
    if record_type == "series":
        return normalize_series_input(payload)
    if record_type == "indicator":
        return normalize_indicator_input(payload)
    if record_type == "theme":
        return normalize_theme_input(payload)
    if record_type == "source_dependency":
        return normalize_source_dependency_input(payload)
    if record_type == "catalog":
        return normalize_catalog_input(payload)
    if record_type == "memory_rule":
        return normalize_memory_rule_input(payload)
    if record_type == "proposal":
        return normalize_proposal_input(payload)
    raise ValueError("Import row requires record_type=series|indicator|theme|source_dependency|catalog|memory_rule|proposal.")


def canonical_record(record: Record) -> Record:
    canonical = deepcopy(record)
    for key in (
        "theme_ids",
        "indicator_ids",
        "input_ids",
        "series_ids",
        "questions",
        "source_dependency_ids",
        "resolved_theme_ids",
        "candidate_theme_ids",
        "candidate_indicator_inputs",
        "memory_rule_ids",
    ):
        if key in canonical:
            canonical[key] = split_list(canonical[key])
    canonical["id"] = str(canonical["id"]).strip()
    canonical["title"] = str(canonical["title"]).strip()
    canonical["status"] = str(canonical.get("status") or "draft").strip() or "draft"
    return canonical


def validate_record(record: Record, approved_records: dict[str, Record]) -> None:
    record_type = record["record_type"]
    if record_type == "series":
        if record.get("source") == "evds" and not record.get("source_version"):
            raise ValueError("EVDS series require source_version before approval.")
        if not record.get("description"):
            raise ValueError("Series records require description before approval.")
        if not record.get("usage"):
            raise ValueError("Series records require usage before approval.")
        return

    if record_type == "indicator":
        inputs = split_list(record.get("input_ids"))
        if not inputs:
            raise ValueError("Indicator records require at least one input_id before approval.")
        missing = [item for item in inputs if item not in approved_records]
        if missing:
            joined = ", ".join(missing)
            record.setdefault("validation_note", "")
            if record["validation_note"]:
                record["validation_note"] += " "
            record["validation_note"] += f"Unresolved input_ids: {joined}"
        if not record.get("formula_expression") and not record.get("formula_description"):
            raise ValueError("Indicator records require a formula expression or description before approval.")
        return

    if record_type == "theme":
        refs = (
            split_list(record.get("series_ids"))
            + split_list(record.get("indicator_ids"))
            + split_list(record.get("source_dependency_ids"))
        )
        missing = [item for item in refs if item not in approved_records]
        if missing:
            joined = ", ".join(missing)
            raise ValueError(f"Theme references are missing from registry: {joined}")
        return

    if record_type == "source_dependency":
        if not record.get("source_kind"):
            raise ValueError("Source dependency records require source_kind before approval.")
        if not record.get("requiredness"):
            raise ValueError("Source dependency records require requiredness before approval.")
        if not record.get("description"):
            raise ValueError("Source dependency records require description before approval.")
        if not record.get("usage"):
            raise ValueError("Source dependency records require usage before approval.")
        refs = split_list(record.get("theme_ids")) + split_list(record.get("indicator_ids"))
        missing = [item for item in refs if item not in approved_records]
        if missing:
            joined = ", ".join(missing)
            raise ValueError(f"Source dependency references are missing from registry: {joined}")
        return

    if record_type == "catalog":
        if not record.get("source_version"):
            raise ValueError("Catalog records require source_version.")
        if not record.get("ticker"):
            raise ValueError("Catalog records require ticker.")
        return

    if record_type == "memory_rule":
        if not record.get("scope"):
            raise ValueError("Memory rules require scope.")
        if not record.get("match_pattern"):
            raise ValueError("Memory rules require match_pattern.")
        return

    if record_type == "proposal":
        if not record.get("target_id"):
            raise ValueError("Proposals require target_id.")
        return

    raise ValueError(f"Unknown record_type: {record_type}")


def render_body(record: Record) -> str:
    record_type = record["record_type"]
    title = record["title"]

    if record_type == "series":
        parts = [
            f"# {title}",
            "",
            "## Aciklama",
            record.get("description") or "-",
            "",
            "## Kullanim",
            record.get("usage") or "-",
        ]
        return "\n".join(parts).strip() + "\n"

    if record_type == "indicator":
        parts = [
            f"# {title}",
            "",
            "## Formul",
            record.get("formula_expression") or "-",
            "",
            "## Formul Aciklamasi",
            record.get("formula_description") or "-",
            "",
            "## Ekonomik Anlam",
            record.get("economic_meaning") or "-",
            "",
            "## Dogrulama Notu",
            record.get("validation_note") or "-",
        ]
        return "\n".join(parts).strip() + "\n"

    if record_type == "theme":
        questions = split_list(record.get("questions"))
        source_dependency_ids = split_list(record.get("source_dependency_ids"))
        parts = [
            f"# {title}",
            "",
            "## Aciklama",
            record.get("description") or "-",
            "",
            "## Source Dependencies",
        ]
        if source_dependency_ids:
            parts.extend([f"- {item}" for item in source_dependency_ids])
        else:
            parts.append("-")
        parts.extend(
            [
                "",
                "## Analiz Sorulari",
            ]
        )
        if questions:
            parts.extend([f"- {item}" for item in questions])
        else:
            parts.append("-")
        return "\n".join(parts).strip() + "\n"

    if record_type == "source_dependency":
        parts = [
            f"# {title}",
            "",
            "## Kaynak Turu",
            record.get("source_kind") or "-",
            "",
            "## Zorunluluk",
            record.get("requiredness") or "-",
            "",
            "## Kaynak URI",
            record.get("source_uri") or "-",
            "",
            "## Local Hint",
            record.get("local_hint") or "-",
            "",
            "## Aciklama",
            record.get("description") or "-",
            "",
            "## Kullanim",
            record.get("usage") or "-",
            "",
            "## Dogrulama Notu",
            record.get("validation_note") or "-",
        ]
        return "\n".join(parts).strip() + "\n"

    if record_type == "catalog":
        raw_metadata = record.get("raw_metadata") or {}
        parts = [
            f"# {title}",
            "",
            "## Ticker",
            record.get("ticker") or "-",
            "",
            "## Source Version",
            record.get("source_version") or "-",
            "",
            "## Frequency",
            record.get("frequency") or "-",
            "",
            "## Unit",
            record.get("unit") or "-",
            "",
            "## Category",
            record.get("category") or "-",
            "",
            "## Data Group",
            record.get("data_group") or "-",
            "",
            "## Official URL",
            record.get("official_url") or "-",
            "",
            "## Raw Metadata",
            json.dumps(raw_metadata, ensure_ascii=False, indent=2) if raw_metadata else "-",
        ]
        return "\n".join(parts).strip() + "\n"

    if record_type == "memory_rule":
        parts = [
            f"# {title}",
            "",
            "## Scope",
            record.get("scope") or "-",
            "",
            "## Match Pattern",
            record.get("match_pattern") or "-",
            "",
            "## Target Type",
            record.get("target_type") or "-",
            "",
            "## Notebook Slug",
            record.get("notebook_slug") or "-",
            "",
            "## Resolved Title",
            record.get("resolved_title") or "-",
            "",
            "## Resolved Unit",
            record.get("resolved_unit") or "-",
            "",
            "## Resolved Frequency",
            record.get("resolved_frequency") or "-",
            "",
            "## Resolved Role",
            record.get("resolved_role") or "-",
            "",
            "## Resolved Themes",
        ]
        resolved_themes = split_list(record.get("resolved_theme_ids"))
        if resolved_themes:
            parts.extend([f"- {item}" for item in resolved_themes])
        else:
            parts.append("-")
        parts.extend(
            [
                "",
                "## Formula Hint",
                record.get("resolved_formula_hint") or "-",
                "",
                "## Evidence Source",
                record.get("evidence_source") or "-",
                "",
                "## Approved By",
                record.get("approved_by") or "-",
                "",
                "## Approved At",
                record.get("approved_at") or "-",
                "",
                "## Notes",
                record.get("notes") or "-",
            ]
        )
        return "\n".join(parts).strip() + "\n"

    if record_type == "proposal":
        evidence = record.get("evidence") or {}
        theme_ids = split_list(record.get("candidate_theme_ids"))
        indicator_inputs = split_list(record.get("candidate_indicator_inputs"))
        parts = [
            f"# {title}",
            "",
            "## Target",
            f"{record.get('target_type') or '-'} | {record.get('target_id') or '-'}",
            "",
            "## Notebook",
            record.get("notebook_slug") or "-",
            "",
            "## Candidate Title",
            record.get("candidate_title") or "-",
            "",
            "## Candidate Unit",
            record.get("candidate_unit") or "-",
            "",
            "## Candidate Frequency",
            record.get("candidate_frequency") or "-",
            "",
            "## Candidate Role",
            record.get("candidate_role") or "-",
            "",
            "## Confidence",
            str(record.get("confidence") or 0.0),
            "",
            "## Candidate Themes",
        ]
        if theme_ids:
            parts.extend([f"- {item}" for item in theme_ids])
        else:
            parts.append("-")
        parts.extend(
            [
                "",
                "## Candidate Indicator Inputs",
            ]
        )
        if indicator_inputs:
            parts.extend([f"- {item}" for item in indicator_inputs])
        else:
            parts.append("-")
        parts.extend(
            [
                "",
                "## Formula Hint",
                record.get("candidate_formula_hint") or "-",
                "",
                "## Source",
                record.get("source") or "-",
                "",
                "## Approval Mode",
                record.get("approval_mode") or "-",
                "",
                "## Approval Reason",
                record.get("approval_reason") or "-",
                "",
                "## Notes",
                record.get("notes") or "-",
                "",
                "## Evidence",
                json.dumps(evidence, ensure_ascii=False, indent=2) if evidence else "-",
            ]
        )
        return "\n".join(parts).strip() + "\n"

    raise ValueError(f"Unknown record_type: {record_type}")
