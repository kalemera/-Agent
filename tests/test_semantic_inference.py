from __future__ import annotations

import csv
import json
from io import StringIO
from pathlib import Path

import pytest
import yaml

from evds_registry.cli import main
from evds_registry.evds_catalog import TCMBEVDSCatalogClient, sync_evds_catalog
from evds_registry.llm import DisabledLLMClient
from evds_registry.records import normalize_catalog_input, normalize_memory_rule_input, normalize_proposal_input
from evds_registry.semantic_inference import auto_approve_proposals, infer_notebook_semantics
from evds_registry.storage import RegistryPaths, id_to_filename, write_record


def run_cli(tmp_path: Path, argv: list[str]) -> tuple[int, str, str]:
    out = StringIO()
    err = StringIO()
    code = main(argv, out=out, err=err, cwd=tmp_path)
    return code, out.getvalue(), err.getvalue()


def build_fixture_notebook(tmp_path: Path) -> Path:
    notebook = {
        "cells": [
            {
                "cell_type": "code",
                "source": [
                    "evds_series_to_get = [\n",
                    "  ['TP.HPBITABLO4.1', 'TP.HPBITABLO4.14']\n",
                    "]\n",
                    "df = evds.get_data(evds_series_to_get[0])\n",
                    "df['proxy'] = df['TP_HPBITABLO4_1'] + df['TP_HPBITABLO4_14']\n",
                ],
                "outputs": [
                    {
                        "output_type": "execute_result",
                        "data": {
                            "text/plain": [
                                "{'TP_HPBITABLO4_1': 'TOPLAM YP MEVDUAT (Milyon ABD Dolari)'}"
                            ]
                        },
                        "metadata": {},
                        "execution_count": 1,
                    }
                ],
                "metadata": {},
                "execution_count": 1,
            }
        ],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    notebook_path = tmp_path / "DTH_Blg_V7.ipynb"
    notebook_path.write_text(json.dumps(notebook, ensure_ascii=False), encoding="utf-8")
    return notebook_path


def parse_frontmatter(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    marker = "\n---\n"
    end_index = raw.find(marker, 4)
    return yaml.safe_load(raw[4:end_index])


class StubApprovalLLMClient:
    provider_name = "stub-llm"
    model_name = "stub-model"

    def __init__(self, decisions: dict[str, tuple[str, str]] | None = None):
        self.decisions = decisions or {}

    def is_enabled(self) -> bool:
        return True

    def generate_structured(self, prompt: str, schema: dict) -> dict:
        payload = json.loads(prompt)
        target_id = payload["proposal"]["target_id"]
        decision, reason = self.decisions.get(target_id, ("approve", "Stub LLM approved."))
        return {"decision": decision, "reason": reason}


def test_sync_evds_catalog_is_idempotent(tmp_path: Path):
    paths = RegistryPaths.from_root(tmp_path)
    paths.ensure_layout()

    class FakeCatalogClient(TCMBEVDSCatalogClient):
        def __init__(self):
            super().__init__(source_version="evds2", api_key="", base_url="https://example.invalid/")

        def list_categories(self):  # noqa: D401
            return [{"CATEGORY_ID": "1", "CATEGORY_NAME": "Finans"}]

        def list_datagroups(self, category_id: str = "", group_code: str = ""):
            assert category_id == "1" or not category_id
            return [{"DATAGROUP_CODE": "bie_test", "CATEGORY_NAME": "Finans"}]

        def list_series(self, code: str):
            assert code == "bie_test"
            return [
                {
                    "SERIE_CODE": "TP.TEST.A1",
                    "SERIE_NAME": "Test Seri (Milyon ABD Dolari)",
                    "FREQUENCY_STR": "Haftalik",
                    "DATAGROUP_CODE": "bie_test",
                }
            ]

    synced_first = sync_evds_catalog(paths, source_version="evds2", scope="all", client=FakeCatalogClient())
    synced_second = sync_evds_catalog(paths, source_version="evds2", scope="all", client=FakeCatalogClient())

    assert len(synced_first) == 1
    assert len(synced_second) == 1
    assert len(list(paths.catalog.glob("*.md"))) == 1
    catalog_file = paths.catalog / id_to_filename("catalog:evds2:TP.TEST.A1")
    assert catalog_file.exists()


def test_sync_evds_catalog_supports_modern_evds3_endpoints(tmp_path: Path):
    paths = RegistryPaths.from_root(tmp_path)
    paths.ensure_layout()

    modern_responses = {
        "https://evds3.tcmb.gov.tr/igmevdsms-dis/searchResults?searchVal=TP.HPBITABLO4.3": json.dumps(
            {
                "veriGruplari": [],
                "seriler": [
                    {
                        "serieCode": "TP.HPBITABLO4.3",
                        "serieName": "1.1.1.Gercek Kisiler",
                        "frequencyStr": "HAFTALIK(CUMA)",
                        "metaDataLink": "https://example.invalid/meta.pdf",
                        "dataGroupCode": "bie_hpbitablo4",
                        "dataGroup": {
                            "dataGroupCode": "bie_hpbitablo4",
                            "dataGroupType": "Bankacilik Sektoru Yabanci Para Mevduati",
                            "birimi": "milyon ABD dolari",
                            "category": {"topicTitleTR": "PARA VE BANKA ISTATISTIKLERI (HAFTALIK)"},
                        },
                    }
                ],
            }
        ),
        "https://evds3.tcmb.gov.tr/igmevdsms-dis/categories/withDatagroups/type=json": json.dumps(
            [
                {
                    "CATEGORY_ID": 4502,
                    "TOPIC_TITLE_TR": "PARA VE BANKA ISTATISTIKLERI (HAFTALIK)",
                    "DATAGROUPS": [
                        {
                            "DATAGROUP_CODE": "bie_hpbitablo4",
                            "DATAGROUP_TYPE": "Bankacilik Sektoru Yabanci Para Mevduati",
                            "birimi": "milyon ABD dolari",
                        }
                    ],
                }
            ]
        ),
        "https://evds3.tcmb.gov.tr/igmevdsms-dis/serieList/fe/type=json&code=bie_hpbitablo4": json.dumps(
            [
                {
                    "SERIE_CODE": "TP.HPBITABLO4.3",
                    "SERIE_NAME": "1.1.1.Gercek Kisiler",
                    "FREQUENCY_STR": "HAFTALIK(CUMA)",
                    "DATAGROUP_CODE": "bie_hpbitablo4",
                }
            ]
        ),
    }

    def fetch_text(url: str, headers: dict[str, str]) -> str:
        assert headers["Accept"].startswith("application/json")
        return modern_responses[url]

    client = TCMBEVDSCatalogClient(
        source_version="evds2",
        api_key="",
        base_url="https://evds3.tcmb.gov.tr/igmevdsms-dis/",
        fetch_text=fetch_text,
    )

    synced = sync_evds_catalog(paths, source_version="evds2", scope="ticker:TP.HPBITABLO4.3", client=client)

    assert len(synced) == 1
    record = synced[0]
    assert record["title"] == "1.1.1.Gercek Kisiler"
    assert record["frequency"] == "weekly"
    assert record["unit"] == "milyon ABD dolari"
    assert record["data_group"] == "bie_hpbitablo4"
    assert record["category"] == "PARA VE BANKA ISTATISTIKLERI (HAFTALIK)"


def test_infer_notebook_semantics_uses_catalog_and_generates_review_queue(tmp_path: Path):
    paths = RegistryPaths.from_root(tmp_path)
    paths.ensure_layout()
    notebook_path = build_fixture_notebook(tmp_path)
    write_record(
        paths.catalog,
        normalize_catalog_input(
            {
                "ticker": "TP.HPBITABLO4.14",
                "title": "c. Diger YP Kalemleri (Milyon ABD Dolari)",
                "frequency": "weekly",
                "unit": "Milyon ABD Dolari",
                "source_version": "evds2",
                "data_group": "bie_dth",
                "category": "DTH",
            }
        ),
    )

    artifacts = infer_notebook_semantics(notebook_path, spec="auto", paths=paths)
    proposal_map = {item["target_id"]: item for item in artifacts.proposals}
    target = proposal_map["evds:TP.HPBITABLO4.14"]

    assert target["candidate_title"] == "c. Diger YP Kalemleri (Milyon ABD Dolari)"
    assert target["candidate_unit"] == "Milyon ABD Dolari"
    assert target["candidate_frequency"] == "weekly"
    assert target["status"] == "review_pending"
    assert (paths.proposals / id_to_filename(target["id"])).exists()


def test_memory_rule_affects_analyze_notebook_output(tmp_path: Path):
    paths = RegistryPaths.from_root(tmp_path)
    paths.ensure_layout()
    notebook_path = build_fixture_notebook(tmp_path)
    write_record(
        paths.memory,
        normalize_memory_rule_input(
            {
                "scope": "global",
                "match_pattern": "TP.HPBITABLO4.14",
                "resolved_title": "c. Diger YP Kalemleri (Milyon ABD Dolari)",
                "resolved_unit": "Milyon ABD Dolari",
                "resolved_frequency": "weekly",
                "resolved_role": "currency_split_line",
                "evidence_source": "manual-test",
                "approved_by": "tester",
                "approved_at": "2026-03-10T10:00:00+00:00",
            }
        ),
    )

    code, out, err = run_cli(tmp_path, ["analyze-notebook", "--notebook", str(notebook_path), "--spec", "auto"])
    assert code == 0, err
    assert "tickers: 2" in out

    report_path = tmp_path / "generated" / "DTH_Blg_V7_ticker_report.md"
    report = report_path.read_text(encoding="utf-8")
    assert "TP.HPBITABLO4.14" in report
    assert "c. Diger YP Kalemleri (Milyon ABD Dolari)" in report
    assert "Memory rule applied" in report


def test_review_promote_and_reject_proposals_via_cli(tmp_path: Path):
    paths = RegistryPaths.from_root(tmp_path)
    paths.ensure_layout()
    notebook_path = build_fixture_notebook(tmp_path)
    write_record(
        paths.catalog,
        normalize_catalog_input(
            {
                "ticker": "TP.HPBITABLO4.14",
                "title": "c. Diger YP Kalemleri (Milyon ABD Dolari)",
                "frequency": "weekly",
                "unit": "Milyon ABD Dolari",
                "source_version": "evds2",
            }
        ),
    )

    code, out, err = run_cli(tmp_path, ["infer-notebook-semantics", "--notebook", str(notebook_path), "--spec", "auto"])
    assert code == 0, err
    assert "proposals: 2" in out

    code, out, err = run_cli(tmp_path, ["review-proposals"])
    assert code == 0, err
    assert "evds:TP.HPBITABLO4.14" in out

    proposal_paths = sorted(paths.proposals.glob("*.md"))
    reject_id = parse_frontmatter(proposal_paths[0])["id"]
    promote_id = parse_frontmatter(proposal_paths[1])["id"]

    code, out, err = run_cli(tmp_path, ["reject-proposal", reject_id])
    assert code == 0, err
    assert "proposal rejected" in out

    code, out, err = run_cli(tmp_path, ["promote-proposal", promote_id])
    assert code == 0, err
    assert "memory rule created" in out

    code, out, err = run_cli(tmp_path, ["review-proposals", "--status", "rejected"])
    assert code == 0, err
    assert reject_id in out

    approved_proposal = parse_frontmatter(paths.proposals / id_to_filename(promote_id))
    assert approved_proposal["status"] == "approved"
    assert approved_proposal["promoted_memory_rule_id"]
    assert len(list(paths.memory.glob("*.md"))) == 1
    assert len(list(paths.drafts.glob("*.md"))) == 1


def test_auto_approve_promotes_safe_series_to_canonical_without_drafts(tmp_path: Path):
    paths = RegistryPaths.from_root(tmp_path)
    paths.ensure_layout()
    write_record(
        paths.catalog,
        normalize_catalog_input(
            {
                "ticker": "TP.TEST.A1",
                "title": "EVDS Resmi Test Seri",
                "frequency": "weekly",
                "unit": "Milyon ABD Dolari",
                "source_version": "evds2",
            }
        ),
    )
    proposal = normalize_proposal_input(
        {
            "id": "proposal:test:series:TP_TEST_A1:aaa111",
            "target_type": "series",
            "target_id": "evds:TP.TEST.A1",
            "ticker": "TP.TEST.A1",
            "notebook_slug": "test-notebook",
            "candidate_title": "Test Seri",
            "candidate_unit": "Milyon ABD Dolari",
            "candidate_frequency": "weekly",
            "candidate_role": "stock_component",
            "confidence": 0.95,
            "status": "review_pending",
            "source": "heuristic",
            "catalog_record_id": "catalog:evds2:TP.TEST.A1",
            "evidence": {"catalog_record": {"title": "EVDS Resmi Test Seri"}},
            "notes": "Safe proposal.",
        }
    )
    write_record(paths.proposals, proposal)

    summary = auto_approve_proposals(paths, StubApprovalLLMClient())

    assert summary.approved == 1
    assert summary.manual_review == 0
    assert summary.skipped == 0
    assert len(list(paths.series.glob("*.md"))) == 1
    assert len(list(paths.memory.glob("*.md"))) == 1
    assert len(list(paths.drafts.glob("*.md"))) == 0
    approved_proposal = parse_frontmatter(paths.proposals / id_to_filename(proposal["id"]))
    assert approved_proposal["status"] == "approved"
    assert approved_proposal["approval_mode"] == "auto_llm"
    assert approved_proposal["approval_reason"] == "Stub LLM approved."
    series_record = parse_frontmatter(next(paths.series.glob("*.md")))
    assert series_record["title"] == "EVDS Resmi Test Seri"
    assert "EVDS resmi seri adi: EVDS Resmi Test Seri" in series_record["description"]
    memory_rule = parse_frontmatter(next(paths.memory.glob("*.md")))
    assert memory_rule["resolved_title"] == "EVDS Resmi Test Seri"
    assert memory_rule["resolved_role"] == ""

    second_summary = auto_approve_proposals(paths, StubApprovalLLMClient())
    assert second_summary.approved == 0
    assert second_summary.manual_review == 0
    assert second_summary.skipped == 0
    assert len(list(paths.series.glob("*.md"))) == 1
    assert len(list(paths.memory.glob("*.md"))) == 1


def test_auto_approve_softens_generic_llm_manual_review_into_approval(tmp_path: Path):
    paths = RegistryPaths.from_root(tmp_path)
    paths.ensure_layout()
    proposal = normalize_proposal_input(
        {
            "id": "proposal:test:series:TP.TEST.SOFT:hhh888",
            "target_type": "series",
            "target_id": "evds:TP.TEST.SOFT",
            "ticker": "TP.TEST.SOFT",
            "notebook_slug": "test-notebook",
            "candidate_title": "Soft Seri",
            "candidate_unit": "Milyon ABD Dolari",
            "candidate_frequency": "weekly",
            "candidate_role": "stock_component",
            "confidence": 0.95,
            "status": "review_pending",
            "source": "heuristic",
            "catalog_record_id": "catalog:evds2:TP.TEST.SOFT",
        }
    )
    write_record(paths.proposals, proposal)

    summary = auto_approve_proposals(
        paths,
        StubApprovalLLMClient({"evds:TP.TEST.SOFT": ("manual_review", "LLM requested manual review.")}),
    )

    assert summary.approved == 1
    approved_proposal = parse_frontmatter(paths.proposals / id_to_filename(proposal["id"]))
    assert approved_proposal["status"] == "approved"
    assert approved_proposal["approval_reason"] == "LLM returned no concrete blocker after deterministic safety checks."


def test_auto_approve_marks_risky_series_as_manual_review(tmp_path: Path):
    paths = RegistryPaths.from_root(tmp_path)
    paths.ensure_layout()
    hybrid = normalize_proposal_input(
        {
            "id": "proposal:test:series:TP.TEST.H1:bbb222",
            "target_type": "series",
            "target_id": "evds:TP.TEST.H1",
            "ticker": "TP.TEST.H1",
            "notebook_slug": "test-notebook",
            "candidate_title": "Hybrid Seri",
            "candidate_unit": "Milyon ABD Dolari",
            "candidate_frequency": "weekly",
            "candidate_role": "stock_component",
            "confidence": 0.97,
            "status": "review_pending",
            "source": "hybrid",
        }
    )
    low_conf = normalize_proposal_input(
        {
            "id": "proposal:test:series:TP.TEST.L1:ccc333",
            "target_type": "series",
            "target_id": "evds:TP.TEST.L1",
            "ticker": "TP.TEST.L1",
            "notebook_slug": "test-notebook",
            "candidate_title": "Dusuk Guven",
            "candidate_unit": "Milyon ABD Dolari",
            "candidate_frequency": "weekly",
            "candidate_role": "stock_component",
            "confidence": 0.75,
            "status": "review_pending",
            "source": "heuristic",
        }
    )
    write_record(paths.proposals, hybrid)
    write_record(paths.proposals, low_conf)

    summary = auto_approve_proposals(paths, StubApprovalLLMClient())

    assert summary.approved == 0
    assert summary.manual_review == 2
    assert parse_frontmatter(paths.proposals / id_to_filename(hybrid["id"]))["status"] == "manual_review"
    low_conf_record = parse_frontmatter(paths.proposals / id_to_filename(low_conf["id"]))
    assert low_conf_record["status"] == "manual_review"
    assert "below the auto-approve threshold" in low_conf_record["approval_reason"]


def test_auto_approve_catches_title_unit_conflict_before_llm(tmp_path: Path):
    paths = RegistryPaths.from_root(tmp_path)
    paths.ensure_layout()
    mismatch = normalize_proposal_input(
        {
            "id": "proposal:test:series:TP.TEST.MISMATCH:iii999",
            "target_type": "series",
            "target_id": "evds:TP.TEST.MISMATCH",
            "ticker": "TP.TEST.MISMATCH",
            "notebook_slug": "test-notebook",
            "candidate_title": "Toplam YP Mevduat (Milyon ABD Dolari)",
            "candidate_unit": "Bin TL",
            "candidate_frequency": "weekly",
            "candidate_role": "stock_component",
            "confidence": 0.95,
            "status": "review_pending",
            "source": "heuristic",
        }
    )
    write_record(paths.proposals, mismatch)

    summary = auto_approve_proposals(paths, StubApprovalLLMClient())

    assert summary.approved == 0
    assert summary.manual_review == 1
    mismatch_record = parse_frontmatter(paths.proposals / id_to_filename(mismatch["id"]))
    assert mismatch_record["status"] == "manual_review"
    assert "contradicts candidate_unit" in mismatch_record["approval_reason"]


def test_auto_approve_detects_conflicts_and_skips_non_series(tmp_path: Path):
    paths = RegistryPaths.from_root(tmp_path)
    paths.ensure_layout()
    first = normalize_proposal_input(
        {
            "id": "proposal:test:series:TP.TEST.C1:ddd444",
            "target_type": "series",
            "target_id": "evds:TP.TEST.C1",
            "ticker": "TP.TEST.C1",
            "notebook_slug": "nb-a",
            "candidate_title": "C1 Seri",
            "candidate_unit": "Milyon ABD Dolari",
            "candidate_frequency": "weekly",
            "candidate_role": "stock_component",
            "confidence": 0.96,
            "status": "review_pending",
            "source": "heuristic",
        }
    )
    second = normalize_proposal_input(
        {
            "id": "proposal:test:series:TP.TEST.C1:eee555",
            "target_type": "series",
            "target_id": "evds:TP.TEST.C1",
            "ticker": "TP.TEST.C1",
            "notebook_slug": "nb-b",
            "candidate_title": "C1 Seri",
            "candidate_unit": "Bin TL",
            "candidate_frequency": "weekly",
            "candidate_role": "stock_component",
            "confidence": 0.96,
            "status": "review_pending",
            "source": "heuristic",
        }
    )
    indicator = normalize_proposal_input(
        {
            "id": "proposal:test:indicator:derived_conflict:fff666",
            "target_type": "indicator",
            "target_id": "derived:test-indicator",
            "candidate_title": "Test Indicator",
            "confidence": 0.98,
            "status": "review_pending",
            "source": "heuristic",
        }
    )
    write_record(paths.proposals, first)
    write_record(paths.proposals, second)
    write_record(paths.proposals, indicator)

    summary = auto_approve_proposals(paths, StubApprovalLLMClient())

    assert summary.approved == 0
    assert summary.manual_review == 2
    assert summary.skipped == 1
    first_record = parse_frontmatter(paths.proposals / id_to_filename(first["id"]))
    assert first_record["status"] == "manual_review"
    assert "conflicting proposal values across notebooks" in first_record["approval_reason"]
    indicator_record = parse_frontmatter(paths.proposals / id_to_filename(indicator["id"]))
    assert indicator_record["status"] == "review_pending"


def test_auto_approve_ignores_series_role_only_conflicts_across_notebooks(tmp_path: Path):
    paths = RegistryPaths.from_root(tmp_path)
    paths.ensure_layout()
    for proposal_id, notebook_slug, role in [
        ("proposal:test:series:TP.TEST.R1:aaa001", "nb-a", "reported_output"),
        ("proposal:test:series:TP.TEST.R1:aaa002", "nb-b", "derived_input"),
    ]:
        write_record(
            paths.proposals,
            normalize_proposal_input(
                {
                    "id": proposal_id,
                    "target_type": "series",
                    "target_id": "evds:TP.TEST.R1",
                    "ticker": "TP.TEST.R1",
                    "notebook_slug": notebook_slug,
                    "candidate_title": "EVDS Role-Test Seri",
                    "candidate_unit": "Milyon ABD Dolari",
                    "candidate_frequency": "weekly",
                    "candidate_role": role,
                    "confidence": 0.95,
                    "status": "review_pending",
                    "source": "heuristic",
                    "catalog_record_id": "catalog:evds2:TP.TEST.R1",
                    "evidence": {"catalog_record": {"title": "EVDS Role-Test Seri"}},
                }
            ),
        )

    summary = auto_approve_proposals(paths, StubApprovalLLMClient())

    assert summary.approved == 2
    assert summary.manual_review == 0
    for proposal_file in paths.proposals.glob("*.md"):
        proposal = parse_frontmatter(proposal_file)
        assert proposal["status"] == "approved"


def test_auto_approve_treats_unit_spelling_variants_as_same(tmp_path: Path):
    paths = RegistryPaths.from_root(tmp_path)
    paths.ensure_layout()
    write_record(
        paths.series,
        {
            "record_type": "series",
            "id": "evds:TP.TEST.U1",
            "title": "EVDS Unit-Test Seri",
            "status": "approved",
            "source": "evds",
            "source_version": "evds2",
            "ticker": "TP.TEST.U1",
            "frequency": "weekly",
            "unit": "Milyon ABD Dolari",
            "description": "Test series",
            "usage": "Test usage",
        },
    )
    proposal = normalize_proposal_input(
        {
            "id": "proposal:test:series:TP.TEST.U1:uuu111",
            "target_type": "series",
            "target_id": "evds:TP.TEST.U1",
            "ticker": "TP.TEST.U1",
            "notebook_slug": "nb-u",
            "candidate_title": "EVDS Unit-Test Seri",
            "candidate_unit": "milyon ABD doları",
            "candidate_frequency": "weekly",
            "candidate_role": "stock_component",
            "confidence": 0.95,
            "status": "review_pending",
            "source": "heuristic",
            "catalog_record_id": "catalog:evds2:TP.TEST.U1",
            "evidence": {"catalog_record": {"title": "EVDS Unit-Test Seri"}},
        }
    )
    write_record(paths.proposals, proposal)

    summary = auto_approve_proposals(paths, StubApprovalLLMClient())

    assert summary.approved == 1
    updated = parse_frontmatter(paths.proposals / id_to_filename(proposal["id"]))
    assert updated["status"] == "approved"


def test_auto_approve_detects_existing_memory_rule_conflict_and_requires_llm_in_cli(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    paths = RegistryPaths.from_root(tmp_path)
    paths.ensure_layout()
    proposal = normalize_proposal_input(
        {
            "id": "proposal:test:series:TP.TEST.M1:ggg777",
            "target_type": "series",
            "target_id": "evds:TP.TEST.M1",
            "ticker": "TP.TEST.M1",
            "notebook_slug": "test-notebook",
            "candidate_title": "M1 Seri",
            "candidate_unit": "Milyon ABD Dolari",
            "candidate_frequency": "weekly",
            "candidate_role": "stock_component",
            "confidence": 0.95,
            "status": "review_pending",
            "source": "heuristic",
        }
    )
    write_record(paths.proposals, proposal)
    write_record(
        paths.memory,
        normalize_memory_rule_input(
            {
                "scope": "global",
                "match_pattern": "TP.TEST.M1",
                "target_type": "series",
                "resolved_title": "M1 Seri",
                "resolved_unit": "Milyon ABD Dolari",
                "resolved_frequency": "monthly",
                "resolved_role": "stock_component",
                "evidence_source": "manual-test",
                "approved_by": "tester",
                "approved_at": "2026-03-11T10:00:00+00:00",
            }
        ),
    )

    summary = auto_approve_proposals(paths, StubApprovalLLMClient())
    assert summary.approved == 0
    assert summary.manual_review == 1
    conflicted = parse_frontmatter(paths.proposals / id_to_filename(proposal["id"]))
    assert conflicted["status"] == "manual_review"
    assert "Memory rule" in conflicted["approval_reason"]

    monkeypatch.setenv("LLM_PROVIDER", "disabled")
    monkeypatch.delenv("OLLAMA_MODEL", raising=False)
    monkeypatch.delenv("LLM_MODEL", raising=False)
    code, _, err = run_cli(tmp_path, ["auto-approve-proposals"])
    assert code == 1
    assert "LLM client must be enabled" in err


@pytest.mark.skipif(not (Path(__file__).resolve().parents[1].parent / "Telegram Bot" / "notebooks").exists(), reason="Notebook fixtures are not available in this environment.")
def test_real_yi_inference_produces_weekly_million_usd_proposals(tmp_path: Path):
    paths = RegistryPaths.from_root(tmp_path)
    paths.ensure_layout()
    notebook_root = Path(__file__).resolve().parents[1].parent / "Telegram Bot" / "notebooks"
    notebook_path = notebook_root / "Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb"
    for ticker, title in [
        ("TP.EBONDPIYDEG.S14", "Hanehalki (S.14)"),
        ("TP.YDOSBAPIYDEG.S15", "Hanehalki (S.14) (Finansal Olmayan Kuruluslarca Ihrac Edilen)"),
        ("TP.YDOSBAPIYDEG.S34", "Hanehalki (S.14) (Bankalar Tarafindan Ihrac Edilen)"),
        ("TP.YDOSBAPIYDEG.S53", "Hanehalki (S.14) (Diger Finansal Aracilar Tarafindan Ihrac Edilen)"),
        ("TP.YDOSBAPIYDEG.S72", "Hanehalki (S.14) (Finansal Yardimcilar Tarafindan Ihrac Edilen)"),
    ]:
        write_record(
            paths.catalog,
            normalize_catalog_input(
                {
                    "ticker": ticker,
                    "title": title,
                    "frequency": "weekly",
                    "unit": "Milyon ABD Dolari",
                    "source_version": "evds2",
                    "data_group": "bie_yi",
                    "category": "Yerlilerin Finansal Varliklari",
                }
            ),
        )

    artifacts = infer_notebook_semantics(notebook_path, spec="auto", paths=paths)
    for target_id in [
        "evds:TP.EBONDPIYDEG.S14",
        "evds:TP.YDOSBAPIYDEG.S15",
        "evds:TP.YDOSBAPIYDEG.S34",
        "evds:TP.YDOSBAPIYDEG.S53",
        "evds:TP.YDOSBAPIYDEG.S72",
    ]:
        proposal = next(item for item in artifacts.proposals if item["target_id"] == target_id)
        assert proposal["candidate_frequency"] == "weekly"
        assert proposal["candidate_unit"] == "Milyon ABD Dolari"
