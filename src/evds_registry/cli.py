from __future__ import annotations

import argparse
import csv
import io
import json
from pathlib import Path
from typing import Iterable, TextIO

from .evds_catalog import sync_evds_catalog
from .source_adapters import EVDSAdapter
from .llm import build_llm_client_from_env
from .notebook_analysis import build_dth_notebook_analysis, build_notebook_analysis, write_import_csv, write_markdown_report
from .records import (
    Record,
    canonical_record,
    normalize_import_row,
    normalize_indicator_input,
    normalize_series_input,
    normalize_source_dependency_input,
    normalize_theme_input,
    split_list,
    validate_record,
)
from .semantic_inference import (
    apply_catalog_and_memory,
    auto_approve_proposals,
    backfill_cross_references,
    BackfillSummary,
    generate_implied_proposals,
    ImpliedProposalSummary,
    infer_notebook_semantics,
    promote_proposal,
    reject_proposal,
    review_proposals,
    write_candidate_drafts_csv,
    write_inference_report,
    write_proposals_json,
)
from .storage import (
    RegistryPaths,
    delete_record,
    diff_fields,
    load_catalog,
    load_drafts,
    load_memory_rules,
    load_proposals,
    load_record,
    load_registry,
    write_record,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="registry", description="EVDS ticker registry CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_series = subparsers.add_parser("add-series-draft", help="Create or update a series draft")
    add_series.add_argument("--ticker", required=True)
    add_series.add_argument("--title")
    add_series.add_argument("--description", required=True)
    add_series.add_argument("--usage", required=True)
    add_series.add_argument("--source-version", choices=["evds2", "evds3"], default="")
    add_series.add_argument("--frequency", default="")
    add_series.add_argument("--unit", default="")
    add_series.add_argument("--official-url", default="")
    add_series.add_argument("--theme-id", action="append", default=[])
    add_series.add_argument("--indicator-id", action="append", default=[])

    add_indicator = subparsers.add_parser("add-indicator-draft", help="Create or update an indicator draft")
    add_indicator.add_argument("--title", required=True)
    add_indicator.add_argument("--id", default="")
    add_indicator.add_argument("--input-id", action="append", default=[])
    add_indicator.add_argument("--formula-expression", default="")
    add_indicator.add_argument("--formula-description", default="")
    add_indicator.add_argument("--output-frequency", default="")
    add_indicator.add_argument("--output-unit", default="")
    add_indicator.add_argument("--economic-meaning", default="")
    add_indicator.add_argument("--validation-note", default="")
    add_indicator.add_argument("--theme-id", action="append", default=[])

    add_source_dep = subparsers.add_parser("add-source-dependency-draft", help="Create or update a source dependency draft")
    add_source_dep.add_argument("--title", required=True)
    add_source_dep.add_argument("--id", default="")
    add_source_dep.add_argument("--description", required=True)
    add_source_dep.add_argument("--usage", required=True)
    add_source_dep.add_argument("--source-kind", default="", help="manual_inline | web_scrape | external_file | api")
    add_source_dep.add_argument("--requiredness", default="", help="required | optional")
    add_source_dep.add_argument("--source-uri", default="")
    add_source_dep.add_argument("--local-hint", default="")
    add_source_dep.add_argument("--validation-note", default="")
    add_source_dep.add_argument("--theme-id", action="append", default=[])
    add_source_dep.add_argument("--indicator-id", action="append", default=[])

    add_theme = subparsers.add_parser("add-theme-draft", help="Create or update a theme draft")
    add_theme.add_argument("--title", required=True)
    add_theme.add_argument("--id", default="")
    add_theme.add_argument("--description", required=True)
    add_theme.add_argument("--series-id", action="append", default=[])
    add_theme.add_argument("--indicator-id", action="append", default=[])
    add_theme.add_argument("--source-dependency-id", action="append", default=[])
    add_theme.add_argument("--question", action="append", default=[])

    import_drafts = subparsers.add_parser("import-drafts", help="Import draft records from CSV")
    import_drafts.add_argument("--file", required=True)

    review = subparsers.add_parser("review-drafts", help="Review pending drafts")
    review.add_argument("--id", default="")

    approve = subparsers.add_parser("approve-draft", help="Approve a draft into the canonical registry")
    approve.add_argument("record_id")

    show_map = subparsers.add_parser("show-map", help="Show linked series, indicators, themes, and source dependencies")
    show_map.add_argument("query")

    analyze = subparsers.add_parser("analyze-notebook", help="Generate ticker report and import CSV from a spec-driven notebook analyzer")
    analyze.add_argument("--notebook", required=True)
    analyze.add_argument("--spec", default="auto")
    analyze.add_argument("--report-out", default="")
    analyze.add_argument("--import-out", default="")

    analyze_dth = subparsers.add_parser("analyze-dth-notebook", help="Alias for analyze-notebook --spec dth-blg-v7")
    analyze_dth.add_argument("--notebook", required=True)
    analyze_dth.add_argument("--report-out", default="")
    analyze_dth.add_argument("--import-out", default="")

    sync_catalog = subparsers.add_parser("sync-evds-catalog", help="Sync EVDS catalog metadata into registry/catalog")
    sync_catalog.add_argument("--source-version", choices=["evds2", "evds3"], default="evds2")
    sync_catalog.add_argument("--scope", default="all")

    infer = subparsers.add_parser("infer-notebook-semantics", help="Generate evidence-backed semantic proposals for a notebook")
    infer.add_argument("--notebook", required=True)
    infer.add_argument("--spec", default="auto")
    infer.add_argument("--report-out", default="")
    infer.add_argument("--proposal-json-out", default="")
    infer.add_argument("--draft-csv-out", default="")

    review_proposals_cmd = subparsers.add_parser("review-proposals", help="Review semantic proposals in the queue")
    review_proposals_cmd.add_argument("--status", default="review_pending")
    review_proposals_cmd.add_argument("--notebook", default="")
    review_proposals_cmd.add_argument("--target-type", default="")
    review_proposals_cmd.add_argument("--min-confidence", type=float, default=0.0)

    auto_approve = subparsers.add_parser("auto-approve-proposals", help="LLM-gated auto-approve for safe series proposals")
    auto_approve.add_argument("--notebook", default="")
    auto_approve.add_argument("--target-type", default="", choices=["", "series", "indicator", "theme"], dest="target_type")
    auto_approve.add_argument("--min-confidence", type=float, default=0.90)
    auto_approve.add_argument("--limit", type=int, default=0)

    gen_implied = subparsers.add_parser("generate-implied-proposals", help="Generate proposals for indicator/theme IDs referenced in approved proposals but lacking records")
    gen_implied.add_argument("--target-type", default="", choices=["", "indicator", "theme"], dest="target_type", help="Restrict to a single type (default: both)")

    subparsers.add_parser("backfill-cross-references", help="Populate theme<->source_dependency linkage from proposal evidence")

    subparsers.add_parser("check-conflicts", help="Report tickers with conflicting role/frequency/unit across notebooks")

    fetch = subparsers.add_parser("fetch-series", help="Fetch live observations from EVDS for a ticker")
    fetch.add_argument("ticker", help="EVDS ticker (e.g. TP.DK.USD.A or evds:TP.DK.USD.A)")
    fetch.add_argument("--start", default="", help="Start date (YYYY-MM-DD or YYYY-MM)")
    fetch.add_argument("--end", default="", help="End date (YYYY-MM-DD or YYYY-MM)")
    fetch.add_argument("--format", default="text", choices=["text", "json", "csv"], dest="out_format")
    fetch.add_argument("--out", default="", help="Write output to file")

    promote = subparsers.add_parser("promote-proposal", help="Promote a proposal into semantic memory and a draft record")
    promote.add_argument("proposal_id")

    reject = subparsers.add_parser("reject-proposal", help="Reject a proposal in the review queue")
    reject.add_argument("proposal_id")

    return parser


def main(argv: list[str] | None = None, out: TextIO | None = None, err: TextIO | None = None, cwd: str | Path | None = None) -> int:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass
    parser = build_parser()
    args = parser.parse_args(argv)
    stdout = out or io.StringIO()
    stderr = err or io.StringIO()
    paths = RegistryPaths.from_root(Path(cwd) if cwd else Path.cwd())
    paths.ensure_layout()

    try:
        if args.command == "add-series-draft":
            handle_add_series(args, paths, stdout)
        elif args.command == "add-indicator-draft":
            handle_add_indicator(args, paths, stdout)
        elif args.command == "add-source-dependency-draft":
            handle_add_source_dependency(args, paths, stdout)
        elif args.command == "add-theme-draft":
            handle_add_theme(args, paths, stdout)
        elif args.command == "import-drafts":
            handle_import_drafts(args, paths, stdout)
        elif args.command == "review-drafts":
            handle_review_drafts(args, paths, stdout)
        elif args.command == "approve-draft":
            handle_approve_draft(args, paths, stdout)
        elif args.command == "show-map":
            handle_show_map(args, paths, stdout)
        elif args.command == "analyze-notebook":
            handle_analyze_notebook(args, paths, stdout)
        elif args.command == "analyze-dth-notebook":
            handle_analyze_dth_notebook(args, paths, stdout)
        elif args.command == "sync-evds-catalog":
            handle_sync_evds_catalog(args, paths, stdout)
        elif args.command == "infer-notebook-semantics":
            handle_infer_notebook_semantics(args, paths, stdout)
        elif args.command == "review-proposals":
            handle_review_proposals(args, paths, stdout)
        elif args.command == "auto-approve-proposals":
            handle_auto_approve_proposals(args, paths, stdout)
        elif args.command == "generate-implied-proposals":
            handle_generate_implied_proposals(args, paths, stdout)
        elif args.command == "backfill-cross-references":
            handle_backfill_cross_references(args, paths, stdout)
        elif args.command == "check-conflicts":
            handle_check_conflicts(args, paths, stdout)
        elif args.command == "fetch-series":
            handle_fetch_series(args, paths, stdout)
        elif args.command == "promote-proposal":
            handle_promote_proposal(args, paths, stdout)
        elif args.command == "reject-proposal":
            handle_reject_proposal(args, paths, stdout)
        else:
            parser.error(f"Unknown command: {args.command}")
            return 2
        if out is None:
            print(stdout.getvalue(), end="")
        return 0
    except Exception as exc:  # noqa: BLE001
        stderr.write(f"Error: {exc}\n")
        if err is None:
            print(stderr.getvalue(), end="")
        return 1


def handle_add_series(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    record = normalize_series_input(
        {
            "ticker": args.ticker,
            "title": args.title,
            "description": args.description,
            "usage": args.usage,
            "source_version": args.source_version,
            "frequency": args.frequency,
            "unit": args.unit,
            "official_url": args.official_url,
            "theme_ids": args.theme_id,
            "indicator_ids": args.indicator_id,
        }
    )
    existing = load_record(paths.series, record["id"])
    action = "update" if existing else "create"
    write_record(paths.drafts, record)
    out.write(f"{action} draft saved: {record['id']}\n")


def handle_add_indicator(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    record = normalize_indicator_input(
        {
            "id": args.id,
            "title": args.title,
            "input_ids": args.input_id,
            "formula_expression": args.formula_expression,
            "formula_description": args.formula_description,
            "output_frequency": args.output_frequency,
            "output_unit": args.output_unit,
            "economic_meaning": args.economic_meaning,
            "validation_note": args.validation_note,
            "theme_ids": args.theme_id,
        }
    )
    existing = load_record(paths.indicators, record["id"])
    action = "update" if existing else "create"
    write_record(paths.drafts, record)
    out.write(f"{action} draft saved: {record['id']}\n")


def handle_add_source_dependency(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    record = normalize_source_dependency_input(
        {
            "id": args.id,
            "title": args.title,
            "description": args.description,
            "usage": args.usage,
            "source_kind": args.source_kind,
            "requiredness": args.requiredness,
            "source_uri": args.source_uri,
            "local_hint": args.local_hint,
            "validation_note": args.validation_note,
            "theme_ids": args.theme_id,
            "indicator_ids": args.indicator_id,
        }
    )
    existing = load_record(paths.source_dependencies, record["id"])
    action = "update" if existing else "create"
    write_record(paths.drafts, record)
    out.write(f"{action} draft saved: {record['id']}\n")


def handle_add_theme(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    record = normalize_theme_input(
        {
            "id": args.id,
            "title": args.title,
            "description": args.description,
            "series_ids": args.series_id,
            "indicator_ids": args.indicator_id,
            "source_dependency_ids": args.source_dependency_id,
            "questions": args.question,
        }
    )
    existing = load_record(paths.themes, record["id"])
    action = "update" if existing else "create"
    write_record(paths.drafts, record)
    out.write(f"{action} draft saved: {record['id']}\n")


def handle_import_drafts(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    file_path = Path(args.file)
    if not file_path.is_absolute():
        file_path = paths.root / file_path
    created: list[str] = []
    with file_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if not any(str(value).strip() for value in row.values()):
                continue
            record = normalize_import_row(row)
            write_record(paths.drafts, record)
            created.append(record["id"])
    out.write(f"imported {len(created)} draft(s)\n")
    for record_id in created:
        out.write(f"- {record_id}\n")


def handle_review_drafts(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    registry = load_registry(paths)
    drafts = load_drafts(paths)
    if args.id:
        record = drafts.get(args.id)
        if record is None:
            raise ValueError(f"Draft not found: {args.id}")
        render_single_review(record, registry.get(record["id"]), out)
        return
    if not drafts:
        out.write("No pending drafts.\n")
        return
    for draft in drafts.values():
        render_single_review(draft, registry.get(draft["id"]), out)
        out.write("\n")


def render_single_review(draft: Record, current: Record | None, out: TextIO) -> None:
    action = "update" if current else "create"
    out.write(f"{draft['id']} [{draft['record_type']}] -> {action}\n")
    out.write(f"changed: {', '.join(diff_fields(draft, current))}\n")


def handle_approve_draft(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    drafts = load_drafts(paths)
    draft = drafts.get(args.record_id)
    if draft is None:
        raise ValueError(f"Draft not found: {args.record_id}")
    registry = load_registry(paths)
    validate_record(draft, registry)
    if draft.get("record_type") == "series":
        ticker = str(draft.get("ticker") or "").strip()
        if ticker:
            adapter = EVDSAdapter.from_env()
            if adapter.is_configured():
                meta = adapter.hydrate_metadata(ticker)
                if not meta:
                    out.write(f"WARNING: ticker {ticker} not found in EVDS. Proceeding anyway.\n")
    approved = canonical_record(draft)
    approved["status"] = "approved"
    write_record(paths.canonical_dir(approved["record_type"]), approved)
    delete_record(paths.drafts, approved["id"])
    out.write(f"approved: {approved['id']}\n")


def handle_show_map(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    registry = load_registry(paths)
    record = resolve_query(args.query, registry.values())
    if record is None:
        raise ValueError(f"No approved record matches query: {args.query}")
    if record["record_type"] == "series":
        render_series_map(record, registry, out)
        return
    if record["record_type"] == "indicator":
        render_indicator_map(record, registry, out)
        return
    if record["record_type"] == "theme":
        render_theme_map(record, registry, out)
        return
    if record["record_type"] == "source_dependency":
        render_source_dependency_map(record, registry, out)
        return
    raise ValueError(f"Unknown record type: {record['record_type']}")


def handle_analyze_notebook(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    notebook_path = resolve_path(args.notebook, paths.root)
    report_path, import_path = resolve_analysis_outputs(paths, notebook_path, args.report_out, args.import_out)
    result = build_notebook_analysis(notebook_path, spec=args.spec)
    catalog_index = {
        record["ticker"]: record
        for record in load_catalog(paths).values()
        if record.get("source_version") in {"", result.default_source_version}
    }
    result = apply_catalog_and_memory(result, catalog_index, load_memory_rules(paths))
    write_markdown_report(result, report_path)
    write_import_csv(result, import_path)
    out.write(f"analyzed notebook: {notebook_path}\n")
    out.write(f"spec: {result.spec_slug}\n")
    out.write(f"report: {report_path}\n")
    out.write(f"import_csv: {import_path}\n")
    out.write(f"tickers: {len(result.analyses)}\n")


def handle_analyze_dth_notebook(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    namespace = argparse.Namespace(
        notebook=args.notebook,
        spec="dth-blg-v7",
        report_out=args.report_out,
        import_out=args.import_out,
    )
    handle_analyze_notebook(namespace, paths, out)


def handle_sync_evds_catalog(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    records = sync_evds_catalog(paths, source_version=args.source_version, scope=args.scope)
    out.write(f"synced catalog records: {len(records)}\n")
    for record in records[:20]:
        out.write(f"- {record['id']} | {record['title']}\n")


def handle_infer_notebook_semantics(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    notebook_path = resolve_path(args.notebook, paths.root)
    generated_dir = paths.root / "generated"
    report_path = resolve_path(args.report_out, paths.root) if args.report_out else generated_dir / f"{notebook_path.stem}_semantic_inference_report.md"
    proposal_json_path = resolve_path(args.proposal_json_out, paths.root) if args.proposal_json_out else generated_dir / f"{notebook_path.stem}_semantic_proposals.json"
    draft_csv_path = resolve_path(args.draft_csv_out, paths.root) if args.draft_csv_out else generated_dir / f"{notebook_path.stem}_semantic_draft_candidates.csv"
    artifacts = infer_notebook_semantics(notebook_path, spec=args.spec, paths=paths, llm_client=build_llm_client_from_env())
    write_inference_report(artifacts, report_path)
    write_proposals_json(artifacts.proposals, proposal_json_path)
    write_candidate_drafts_csv(artifacts.proposals, draft_csv_path)
    out.write(f"inferred notebook semantics: {notebook_path}\n")
    out.write(f"spec: {artifacts.analysis_result.spec_slug}\n")
    out.write(f"report: {report_path}\n")
    out.write(f"proposal_json: {proposal_json_path}\n")
    out.write(f"draft_csv: {draft_csv_path}\n")
    out.write(f"proposals: {len(artifacts.proposals)}\n")


def handle_review_proposals(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    proposals = review_proposals(
        paths,
        status=args.status,
        notebook_slug=args.notebook,
        target_type=args.target_type,
        min_confidence=args.min_confidence,
    )
    if not proposals:
        out.write("No proposals matched the filters.\n")
        return
    for proposal in proposals:
        out.write(
            f"{proposal['id']} | {proposal.get('status')} | {proposal.get('target_type')} | {proposal.get('target_id')} | "
            f"{proposal.get('confidence')} | {proposal.get('candidate_title') or '-'}\n"
        )


def handle_auto_approve_proposals(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    llm_client = build_llm_client_from_env()
    series_only = args.target_type == "series" or not args.target_type
    if series_only and not llm_client.is_enabled():
        raise ValueError("LLM client must be enabled for auto-approve of series proposals.")
    summary = auto_approve_proposals(
        paths,
        llm_client,
        notebook_slug=args.notebook,
        target_type=args.target_type,
        min_confidence=args.min_confidence,
        limit=args.limit,
    )
    out.write(f"approved: {summary.approved}\n")
    out.write(f"manual_review: {summary.manual_review}\n")
    out.write(f"skipped: {summary.skipped}\n")


def handle_generate_implied_proposals(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    target_types = [args.target_type] if args.target_type else None
    summary = generate_implied_proposals(paths, target_types=target_types)
    out.write(f"created: {summary.created}\n")
    out.write(f"skipped_existing: {summary.skipped_existing}\n")


def handle_backfill_cross_references(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    summary = backfill_cross_references(paths)
    out.write(f"themes_updated: {summary.themes_updated}\n")
    out.write(f"source_deps_updated: {summary.source_deps_updated}\n")


def handle_check_conflicts(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    proposals = load_proposals(paths)
    ticker_notebooks: dict[str, list[dict[str, str]]] = {}
    for p in proposals.values():
        if p.get("status") != "approved" or p.get("target_type") != "series":
            continue
        ticker = str(p.get("ticker") or "").strip()
        if not ticker:
            continue
        ticker_notebooks.setdefault(ticker, []).append({
            "notebook": str(p.get("notebook_slug") or "-"),
            "role": str(p.get("candidate_role") or "-"),
            "frequency": str(p.get("candidate_frequency") or "-"),
            "unit": str(p.get("candidate_unit") or "-"),
        })
    conflict_count = 0
    for ticker in sorted(ticker_notebooks):
        entries = ticker_notebooks[ticker]
        if len(entries) < 2:
            continue
        roles = {e["role"] for e in entries}
        freqs = {e["frequency"] for e in entries}
        units = {e["unit"] for e in entries}
        diffs = []
        if len(roles) > 1:
            diffs.append(f"role: {', '.join(sorted(roles))}")
        if len(freqs) > 1:
            diffs.append(f"frequency: {', '.join(sorted(freqs))}")
        if len(units) > 1:
            diffs.append(f"unit: {', '.join(sorted(units))}")
        if diffs:
            conflict_count += 1
            notebooks = ", ".join(e["notebook"] for e in entries)
            out.write(f"CONFLICT {ticker} [{notebooks}]\n")
            for d in diffs:
                out.write(f"  {d}\n")
    if conflict_count == 0:
        out.write("No conflicts found.\n")
    else:
        out.write(f"\n{conflict_count} conflict(s) found.\n")


def handle_fetch_series(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    adapter = EVDSAdapter.from_env()
    if not adapter.is_configured():
        raise ValueError("EVDS_API_KEY must be set in .env for fetch-series.")
    ticker = args.ticker.removeprefix("evds:").strip()
    registry = load_registry(paths)
    registry_record = registry.get(f"evds:{ticker}")
    meta = adapter.hydrate_metadata(ticker)
    if not meta and not registry_record:
        raise ValueError(f"Ticker {ticker} not found in EVDS or registry.")
    out.write(f"Ticker: {ticker}\n")
    if meta:
        out.write(f"EVDS Title: {meta.get('title', '-')}\n")
        out.write(f"Frequency: {meta.get('frequency', '-')}\n")
        out.write(f"Unit: {meta.get('unit', '-')}\n")
        out.write(f"Data Group: {meta.get('data_group', '-')}\n")
        out.write(f"Category: {meta.get('category', '-')}\n")
    if registry_record:
        out.write(f"Registry Title: {registry_record.get('title', '-')}\n")
        out.write(f"Registry Status: {registry_record.get('status', '-')}\n")
    if not meta:
        out.write("WARNING: not found in EVDS (API may be unavailable)\n")
    out.write("\nNote: live data fetch unavailable (TCMB evds2 API deprecated). Use evds-mcp when ready.\n")


def handle_promote_proposal(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    draft_record, memory_rule = promote_proposal(paths, args.proposal_id)
    if draft_record is not None:
        out.write(f"draft created: {draft_record['id']}\n")
    out.write(f"memory rule created: {memory_rule['id']}\n")
    out.write(f"proposal approved: {args.proposal_id}\n")


def handle_reject_proposal(args: argparse.Namespace, paths: RegistryPaths, out: TextIO) -> None:
    proposal = reject_proposal(paths, args.proposal_id)
    out.write(f"proposal rejected: {proposal['id']}\n")


def resolve_analysis_outputs(paths: RegistryPaths, notebook_path: Path, report_out: str, import_out: str) -> tuple[Path, Path]:
    generated_dir = paths.root / "generated"
    report_path = Path(report_out) if report_out else generated_dir / f"{notebook_path.stem}_ticker_report.md"
    import_path = Path(import_out) if import_out else generated_dir / f"{notebook_path.stem}_registry_import.csv"
    return resolve_path(report_path, paths.root), resolve_path(import_path, paths.root)


def resolve_path(pathlike: str | Path, root: Path) -> Path:
    path = Path(pathlike)
    return path if path.is_absolute() else root / path


def resolve_query(query: str, records: Iterable[Record]) -> Record | None:
    query = query.strip()
    by_id: dict[str, Record] = {}
    for record in records:
        by_id[record["id"]] = record
        if record["record_type"] == "series":
            by_id[record["ticker"]] = record
        by_id[record["id"].split(":", 1)[-1]] = record
    return by_id.get(query)


def render_series_map(record: Record, registry: dict[str, Record], out: TextIO) -> None:
    indicator_ids = set(split_list(record.get("indicator_ids")))
    theme_ids = set(split_list(record.get("theme_ids")))
    for item in registry.values():
        if item["record_type"] == "indicator" and record["id"] in split_list(item.get("input_ids")):
            indicator_ids.add(item["id"])
            theme_ids.update(split_list(item.get("theme_ids")))
        if item["record_type"] == "theme" and record["id"] in split_list(item.get("series_ids")):
            theme_ids.add(item["id"])
    source_dependency_ids = collect_source_dependency_ids(theme_ids, indicator_ids, registry)

    out.write(f"Series: {record['title']}\n")
    out.write(f"ID: {record['id']}\n")
    out.write(f"Ticker: {record['ticker']}\n")
    out.write(f"Source Version: {record.get('source_version') or '-'}\n")
    out.write(f"Description: {record.get('description') or '-'}\n")
    out.write(f"Usage: {record.get('usage') or '-'}\n")
    out.write("\nLinked Indicators:\n")
    render_related(indicator_ids, registry, out)
    out.write("\nLinked Themes:\n")
    render_related(theme_ids, registry, out)
    out.write("\nLinked Source Dependencies:\n")
    render_related(source_dependency_ids, registry, out)
    render_provenance_sections(record, out)


def render_indicator_map(record: Record, registry: dict[str, Record], out: TextIO) -> None:
    theme_ids = set(split_list(record.get("theme_ids")))
    for item in registry.values():
        if item["record_type"] == "theme" and record["id"] in split_list(item.get("indicator_ids")):
            theme_ids.add(item["id"])
    source_dependency_ids = collect_source_dependency_ids(theme_ids, {record["id"]}, registry)

    out.write(f"Indicator: {record['title']}\n")
    out.write(f"ID: {record['id']}\n")
    out.write(f"Formula: {record.get('formula_expression') or '-'}\n")
    out.write(f"Formula Note: {record.get('formula_description') or '-'}\n")
    out.write(f"Economic Meaning: {record.get('economic_meaning') or '-'}\n")
    out.write("\nInputs:\n")
    render_related(split_list(record.get("input_ids")), registry, out)
    out.write("\nLinked Themes:\n")
    render_related(theme_ids, registry, out)
    out.write("\nLinked Source Dependencies:\n")
    render_related(source_dependency_ids, registry, out)
    render_provenance_sections(record, out)


def render_theme_map(record: Record, registry: dict[str, Record], out: TextIO) -> None:
    series_ids = set(split_list(record.get("series_ids")))
    indicator_ids = set(split_list(record.get("indicator_ids")))
    source_dependency_ids = set(split_list(record.get("source_dependency_ids")))
    for item in registry.values():
        if item["record_type"] == "series" and record["id"] in split_list(item.get("theme_ids")):
            series_ids.add(item["id"])
        if item["record_type"] == "indicator" and record["id"] in split_list(item.get("theme_ids")):
            indicator_ids.add(item["id"])
        if item["record_type"] == "source_dependency" and record["id"] in split_list(item.get("theme_ids")):
            source_dependency_ids.add(item["id"])

    out.write(f"Theme: {record['title']}\n")
    out.write(f"ID: {record['id']}\n")
    out.write(f"Description: {record.get('description') or '-'}\n")
    out.write("\nSeries:\n")
    render_related(series_ids, registry, out)
    out.write("\nIndicators:\n")
    render_related(indicator_ids, registry, out)
    out.write("\nSource Dependencies:\n")
    render_related(source_dependency_ids, registry, out)
    out.write("\nQuestions:\n")
    questions = split_list(record.get("questions"))
    if questions:
        for question in questions:
            out.write(f"- {question}\n")
    else:
        out.write("-\n")
    render_provenance_sections(record, out)


def render_source_dependency_map(record: Record, registry: dict[str, Record], out: TextIO) -> None:
    theme_ids = set(split_list(record.get("theme_ids")))
    indicator_ids = set(split_list(record.get("indicator_ids")))
    series_ids: set[str] = set()
    for item in registry.values():
        if item["record_type"] == "theme" and record["id"] in split_list(item.get("source_dependency_ids")):
            theme_ids.add(item["id"])
            series_ids.update(split_list(item.get("series_ids")))
            indicator_ids.update(split_list(item.get("indicator_ids")))
        if item["record_type"] == "indicator" and record["id"] in split_list(item.get("input_ids")):
            indicator_ids.add(item["id"])
            theme_ids.update(split_list(item.get("theme_ids")))
        if item["record_type"] == "series" and any(theme_id in split_list(item.get("theme_ids")) for theme_id in theme_ids):
            series_ids.add(item["id"])

    out.write(f"Source Dependency: {record['title']}\n")
    out.write(f"ID: {record['id']}\n")
    out.write(f"Source Kind: {record.get('source_kind') or '-'}\n")
    out.write(f"Requiredness: {record.get('requiredness') or '-'}\n")
    out.write(f"Description: {record.get('description') or '-'}\n")
    out.write(f"Usage: {record.get('usage') or '-'}\n")
    out.write("\nLinked Themes:\n")
    render_related(theme_ids, registry, out)
    out.write("\nLinked Indicators:\n")
    render_related(indicator_ids, registry, out)
    out.write("\nImpacted Series:\n")
    render_related(series_ids, registry, out)
    render_provenance_sections(record, out)


def collect_source_dependency_ids(theme_ids: set[str], indicator_ids: set[str], registry: dict[str, Record]) -> set[str]:
    source_dependency_ids: set[str] = set()
    for theme_id in theme_ids:
        theme = registry.get(theme_id)
        if theme and theme["record_type"] == "theme":
            source_dependency_ids.update(split_list(theme.get("source_dependency_ids")))
    for item in registry.values():
        if item["record_type"] != "source_dependency":
            continue
        if theme_ids.intersection(split_list(item.get("theme_ids"))):
            source_dependency_ids.add(item["id"])
        if indicator_ids.intersection(split_list(item.get("indicator_ids"))):
            source_dependency_ids.add(item["id"])
    return source_dependency_ids


def render_provenance_sections(record: Record, out: TextIO) -> None:
    target_id = record["id"]
    root = Path(record.get("path", ".")).resolve().parents[2] if record.get("path") else Path.cwd()
    paths = RegistryPaths.from_root(root)
    proposals = [
        proposal
        for proposal in load_proposals(paths).values()
        if proposal.get("target_id") == target_id
    ]
    memory_rules = [
        rule
        for rule in load_memory_rules(paths).values()
        if split_list(rule.get("resolved_theme_ids"))
        or any(
            key in {record.get("ticker"), record["id"], record["id"].split(":", 1)[-1]}
            for key in {rule.get("match_pattern"), rule.get("resolved_title")}
        )
        or rule.get("match_pattern") in {record.get("ticker"), record["id"], family_prefix(record)}
    ]
    out.write("\nProposal Provenance:\n")
    if proposals:
        for proposal in sorted(proposals, key=lambda item: item["id"]):
            out.write(f"- {proposal['id']} | {proposal.get('status')} | {proposal.get('confidence')}\n")
    else:
        out.write("-\n")
    out.write("\nMemory Rules:\n")
    if memory_rules:
        for rule in sorted(memory_rules, key=lambda item: item["id"]):
            out.write(f"- {rule['id']} | {rule.get('evidence_source') or '-'}\n")
    else:
        out.write("-\n")


def family_prefix(record: Record) -> str:
    ticker = str(record.get("ticker") or "")
    if ticker:
        return ticker.split(".", 2)[0] + "." + ticker.split(".", 2)[1] if "." in ticker else ticker
    return record["id"]


def render_related(record_ids: Iterable[str], registry: dict[str, Record], out: TextIO) -> None:
    ids = sorted({record_id for record_id in record_ids if record_id})
    if not ids:
        out.write("-\n")
        return
    for record_id in ids:
        record = registry.get(record_id)
        if record is None:
            out.write(f"- {record_id} [missing]\n")
            continue
        out.write(f"- {record_id} | {record.get('title')}\n")


if __name__ == "__main__":
    raise SystemExit(main())
