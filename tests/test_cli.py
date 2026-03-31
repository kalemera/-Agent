from __future__ import annotations

import csv
from io import StringIO

import yaml

from evds_registry.cli import main
from evds_registry.storage import id_to_filename


def parse_frontmatter(path):
    raw = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    marker = "\n---\n"
    end_index = raw.find(marker, 4)
    return yaml.safe_load(raw[4:end_index])


def run_cli(tmp_path, argv):
    out = StringIO()
    err = StringIO()
    code = main(argv, out=out, err=err, cwd=tmp_path)
    return code, out.getvalue(), err.getvalue()


def test_chat_and_bulk_create_same_series_draft(tmp_path):
    code, _, err = run_cli(
        tmp_path,
        [
            "add-series-draft",
            "--ticker",
            "TP.FE.OKG01",
            "--title",
            "TUFE",
            "--description",
            "TUFE endeksi",
            "--usage",
            "Enflasyon izlemede kullanirim",
            "--source-version",
            "evds2",
            "--frequency",
            "monthly",
            "--unit",
            "index",
            "--theme-id",
            "theme:inflation",
            "--indicator-id",
            "derived:cpi-yoy",
        ],
    )
    assert code == 0, err

    chat_path = tmp_path / "drafts" / id_to_filename("evds:TP.FE.OKG01")
    chat_record = parse_frontmatter(chat_path)
    chat_path.unlink()

    import_file = tmp_path / "series.csv"
    with import_file.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "record_type",
                "title",
                "ticker",
                "source_version",
                "frequency",
                "unit",
                "description",
                "usage",
                "theme_ids",
                "indicator_ids",
            ],
        )
        writer.writeheader()
        writer.writerow(
            {
                "record_type": "series",
                "title": "TUFE",
                "ticker": "TP.FE.OKG01",
                "source_version": "evds2",
                "frequency": "monthly",
                "unit": "index",
                "description": "TUFE endeksi",
                "usage": "Enflasyon izlemede kullanirim",
                "theme_ids": "theme:inflation",
                "indicator_ids": "derived:cpi-yoy",
            }
        )

    code, _, err = run_cli(tmp_path, ["import-drafts", "--file", str(import_file)])
    assert code == 0, err
    bulk_record = parse_frontmatter(tmp_path / "drafts" / id_to_filename("evds:TP.FE.OKG01"))
    assert bulk_record == chat_record


def test_duplicate_ticker_updates_existing_canonical_flow(tmp_path):
    code, _, err = run_cli(
        tmp_path,
        [
            "add-series-draft",
            "--ticker",
            "TP.FE.OKG01",
            "--description",
            "TUFE endeksi",
            "--usage",
            "Enflasyon izlemede kullanirim",
            "--source-version",
            "evds3",
        ],
    )
    assert code == 0, err
    code, _, err = run_cli(tmp_path, ["approve-draft", "evds:TP.FE.OKG01"])
    assert code == 0, err

    code, out, err = run_cli(
        tmp_path,
        [
            "add-series-draft",
            "--ticker",
            "TP.FE.OKG01",
            "--description",
            "Guncellenmis aciklama",
            "--usage",
            "Enflasyon izlemede kullanirim",
            "--source-version",
            "evds3",
        ],
    )
    assert code == 0, err
    assert "update draft saved" in out
    assert len(list((tmp_path / "registry" / "series").glob("*.md"))) == 1
    assert len(list((tmp_path / "drafts").glob("*.md"))) == 1


def test_add_indicator_and_theme_drafts_support_user_defined_workflow(tmp_path):
    for ticker in ["TP.FE.OKG01", "TP.FE.OKG02"]:
        code, _, err = run_cli(
            tmp_path,
            [
                "add-series-draft",
                "--ticker",
                ticker,
                "--description",
                f"{ticker} aciklamasi",
                "--usage",
                "Gosterge girdisi",
                "--source-version",
                "evds2",
            ],
        )
        assert code == 0, err
        code, _, err = run_cli(tmp_path, ["approve-draft", f"evds:{ticker}"])
        assert code == 0, err

    code, _, err = run_cli(
        tmp_path,
        [
            "add-indicator-draft",
            "--id",
            "derived:sample-household-fx",
            "--title",
            "Ornek hanehalki doviz gostergesi",
            "--input-id",
            "evds:TP.FE.OKG01",
            "--input-id",
            "evds:TP.FE.OKG02",
            "--formula-expression",
            "evds:TP.FE.OKG01 + evds:TP.FE.OKG02",
            "--output-frequency",
            "weekly",
            "--output-unit",
            "Milyon ABD Dolari",
            "--economic-meaning",
            "Ornek brut doviz varlik proxy gostergesi",
            "--validation-note",
            "Net pozisyon degildir.",
            "--theme-id",
            "theme:household-fx-assets",
        ],
    )
    assert code == 0, err
    indicator_record = parse_frontmatter(tmp_path / "drafts" / id_to_filename("derived:sample-household-fx"))
    assert indicator_record["input_ids"] == ["evds:TP.FE.OKG01", "evds:TP.FE.OKG02"]
    assert indicator_record["output_frequency"] == "weekly"

    code, _, err = run_cli(tmp_path, ["approve-draft", "derived:sample-household-fx"])
    assert code == 0, err

    code, _, err = run_cli(
        tmp_path,
        [
            "add-theme-draft",
            "--id",
            "theme:household-fx-assets",
            "--title",
            "Hanehalki Doviz Varliklari",
            "--description",
            "Mevduat ve menkul kiymet bilesenleri",
            "--series-id",
            "evds:TP.FE.OKG01",
            "--series-id",
            "evds:TP.FE.OKG02",
            "--indicator-id",
            "derived:sample-household-fx",
            "--question",
            "Hanehalkinin doviz varliklari nasil degisiyor?",
        ],
    )
    assert code == 0, err
    theme_record = parse_frontmatter(tmp_path / "drafts" / id_to_filename("theme:household-fx-assets"))
    assert theme_record["series_ids"] == ["evds:TP.FE.OKG01", "evds:TP.FE.OKG02"]
    assert theme_record["indicator_ids"] == ["derived:sample-household-fx"]

    code, _, err = run_cli(tmp_path, ["approve-draft", "theme:household-fx-assets"])
    assert code == 0, err

    code, out, err = run_cli(tmp_path, ["show-map", "derived:sample-household-fx"])
    assert code == 0, err
    assert "theme:household-fx-assets" in out


def test_indicator_approval_requires_existing_inputs(tmp_path):
    import_file = tmp_path / "indicator.csv"
    with import_file.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["record_type", "id", "title", "input_ids", "formula_expression"],
        )
        writer.writeheader()
        writer.writerow(
            {
                "record_type": "indicator",
                "id": "derived:cpi-yoy",
                "title": "TUFE yillik degisim",
                "input_ids": "evds:TP.FE.OKG01",
                "formula_expression": "(x_t / x_t-12 - 1) * 100",
            }
        )

    code, _, err = run_cli(tmp_path, ["import-drafts", "--file", str(import_file)])
    assert code == 0, err
    code, _, err = run_cli(tmp_path, ["approve-draft", "derived:cpi-yoy"])
    assert code == 1
    assert "missing from registry" in err


def test_theme_and_source_dependency_show_map(tmp_path):
    records = tmp_path / "records.csv"
    with records.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "record_type",
                "id",
                "title",
                "ticker",
                "source_version",
                "description",
                "usage",
                "theme_ids",
                "series_ids",
                "indicator_ids",
                "input_ids",
                "formula_expression",
                "questions",
                "source_dependency_ids",
                "source_kind",
                "requiredness",
                "source_uri",
                "local_hint",
            ],
        )
        writer.writeheader()
        writer.writerow(
            {
                "record_type": "series",
                "title": "TUFE",
                "ticker": "TP.FE.OKG01",
                "source_version": "evds2",
                "description": "TUFE endeksi",
                "usage": "Enflasyon izlemede kullanirim",
                "theme_ids": "theme:inflation",
                "indicator_ids": "derived:cpi-yoy",
            }
        )
        writer.writerow(
            {
                "record_type": "series",
                "title": "TUFE cekirdek",
                "ticker": "TP.FE.OKG02",
                "source_version": "evds2",
                "description": "Cekirdek TUFE",
                "usage": "Enflasyon izlemede kullanirim",
                "theme_ids": "theme:inflation",
            }
        )
        writer.writerow(
            {
                "record_type": "indicator",
                "id": "derived:cpi-yoy",
                "title": "TUFE yillik degisim",
                "input_ids": "evds:TP.FE.OKG01|evds:TP.FE.OKG02",
                "formula_expression": "(x_t / x_t-12 - 1) * 100",
                "theme_ids": "theme:inflation",
            }
        )
        writer.writerow(
            {
                "record_type": "source_dependency",
                "id": "source:legacy-xlsx",
                "title": "Legacy XLSX",
                "description": "Eski seri backfill dosyasi",
                "usage": "Temaya arka plan saglar",
                "source_kind": "excel_local",
                "requiredness": "required_input",
                "source_uri": "https://example.com/legacy.xlsx",
                "local_hint": "data/legacy.xlsx",
            }
        )
        writer.writerow(
            {
                "record_type": "theme",
                "id": "theme:inflation",
                "title": "Enflasyon",
                "description": "Enflasyon temasi",
                "series_ids": "evds:TP.FE.OKG01|evds:TP.FE.OKG02",
                "indicator_ids": "derived:cpi-yoy",
                "source_dependency_ids": "source:legacy-xlsx",
                "questions": "Enflasyon ne durumda?|Temel egilim ne soyluyor?",
            }
        )

    code, _, err = run_cli(tmp_path, ["import-drafts", "--file", str(records)])
    assert code == 0, err
    for record_id in [
        "evds:TP.FE.OKG01",
        "evds:TP.FE.OKG02",
        "derived:cpi-yoy",
        "source:legacy-xlsx",
        "theme:inflation",
    ]:
        code, _, err = run_cli(tmp_path, ["approve-draft", record_id])
        assert code == 0, err

    code, out, err = run_cli(tmp_path, ["show-map", "theme:inflation"])
    assert code == 0, err
    assert "evds:TP.FE.OKG01 | TUFE" in out
    assert "derived:cpi-yoy | TUFE yillik degisim" in out
    assert "source:legacy-xlsx | Legacy XLSX" in out

    code, out, err = run_cli(tmp_path, ["show-map", "TP.FE.OKG01"])
    assert code == 0, err
    assert "theme:inflation | Enflasyon" in out
    assert "derived:cpi-yoy | TUFE yillik degisim" in out
    assert "source:legacy-xlsx | Legacy XLSX" in out

    code, out, err = run_cli(tmp_path, ["show-map", "source:legacy-xlsx"])
    assert code == 0, err
    assert "theme:inflation | Enflasyon" in out
    assert "evds:TP.FE.OKG01 | TUFE" in out


def test_evds_series_requires_source_version_before_approval(tmp_path):
    code, _, err = run_cli(
        tmp_path,
        [
            "add-series-draft",
            "--ticker",
            "TP.FE.OKG01",
            "--description",
            "TUFE endeksi",
            "--usage",
            "Enflasyon izlemede kullanirim",
        ],
    )
    assert code == 0, err
    code, _, err = run_cli(tmp_path, ["approve-draft", "evds:TP.FE.OKG01"])
    assert code == 1
    assert "source_version" in err
