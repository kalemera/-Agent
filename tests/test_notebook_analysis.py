from __future__ import annotations

import json
from io import StringIO

from evds_registry.cli import main
from evds_registry.notebook_analysis import build_dth_notebook_analysis, build_notebook_analysis, extract_unit, fix_mojibake


HPBITABLO2_CODES = [
    "TP.HPBITABLO2.1",
    "TP.HPBITABLO2.2",
    "TP.HPBITABLO2.3",
    "TP.HPBITABLO2.3",
    "TP.HPBITABLO2.4",
    "TP.HPBITABLO2.5",
    "TP.HPBITABLO2.6",
    "TP.HPBITABLO2.7",
    "TP.HPBITABLO2.8",
    "TP.HPBITABLO2.10",
    "TP.HPBITABLO2.11",
    "TP.HPBITABLO2.12",
    "TP.HPBITABLO2.13",
    "TP.HPBITABLO2.14",
    "TP.HPBITABLO2.15",
    "TP.HPBITABLO2.16",
    "TP.HPBITABLO2.17",
    "TP.HPBITABLO2.18",
    "TP.HPBITABLO2.19",
    "TP.HPBITABLO2.20",
    "TP.HPBITABLO2.21",
    "TP.HPBITABLO2.22",
    "TP.HPBITABLO2.23",
    "TP.HPBITABLO2.24",
    "TP.HPBITABLO2.28",
    "TP.HPBITABLO2.32",
    "TP.HPBITABLO2.33",
    "TP.HPBITABLO2.34",
]
HPBITABLO3_CODES = [
    "TP.HPBITABLO3.1",
    "TP.HPBITABLO3.2",
    "TP.HPBITABLO3.18",
    "TP.HPBITABLO3.21",
    "TP.HPBITABLO3.24",
]
HPBITABLO4_CODES = [
    "TP.HPBITABLO4.1",
    "TP.HPBITABLO4.2",
    "TP.HPBITABLO4.3",
    "TP.HPBITABLO4.4",
    "TP.HPBITABLO4.5",
    "TP.HPBITABLO4.6",
    "TP.HPBITABLO4.7",
    "TP.HPBITABLO4.8",
    "TP.HPBITABLO4.9",
    "TP.HPBITABLO4.10",
    "TP.HPBITABLO4.11",
    "TP.HPBITABLO4.12",
    "TP.HPBITABLO4.13",
    "TP.HPBITABLO4.14",
    "TP.HPBITABLO4.15",
    "TP.HPBITABLO4.16",
    "TP.HPBITABLO4.17",
    "TP.HPBITABLO4.18",
    "TP.HPBITABLO4.19",
    "TP.HPBITABLO4.20",
    "TP.HPBITABLO4.21",
]
SERIE_NAME_OVERRIDES = {
    "TP.HPBITABLO2.1": "A. TOPLAM MEVDUAT (Bin TL)",
    "TP.HPBITABLO2.2": "1. Yurt Ici Yerlesikler (Bin TL)",
    "TP.HPBITABLO2.3": "a. TL (Bin TL)",
    "TP.HPBITABLO2.6": "b. YP (Bin TL)",
    "TP.HPBITABLO2.13": "2. Yurt Ici Yerlesik Bankalar (Bin TL)",
    "TP.HPBITABLO2.14": "a. TL (Bin TL)",
    "TP.HPBITABLO2.15": "b. YP (Bin TL)",
    "TP.HPBITABLO2.16": "3. Yurt Disi Yerlesikler (Bin TL)",
    "TP.HPBITABLO2.17": "a. TL (Bin TL)",
    "TP.HPBITABLO2.18": "b. YP (Bin TL)",
    "TP.HPBITABLO2.19": "4. Yurt Disi Yerlesik Bankalar (Bin TL)",
    "TP.HPBITABLO2.20": "a. TL (Bin TL)",
    "TP.HPBITABLO2.21": "b. YP (Bin TL)",
    "TP.HPBITABLO2.22": "B. TOPLAM KREDI (Bin TL)",
    "TP.HPBITABLO2.23": "1. Yurt Ici Yerlesikler (Bin TL)",
    "TP.HPBITABLO2.24": "a. TL (Bin TL)",
    "TP.HPBITABLO2.28": "b. YP (Bin TL)",
    "TP.HPBITABLO2.32": "2. Yurt Ici Yerlesik Finansal Kuruluslar (Bin TL)",
    "TP.HPBITABLO2.33": "a. TL (Bin TL)",
    "TP.HPBITABLO2.34": "b. YP (Bin TL)",
    "TP.HPBITABLO3.1": "TOPLAM TL MEVDUAT (Bin TL)",
    "TP.HPBITABLO3.2": "A. Yurt Ici Yerlesikler (Bin TL)",
    "TP.HPBITABLO3.18": "B. Yurt Ici Yerlesik Bankalar (Bin TL)",
    "TP.HPBITABLO3.21": "C. Yurt Disi Yerlesikler (Bin TL)",
    "TP.HPBITABLO3.24": "D. Yurt Disi Yerlesik Bankalar (Bin TL)",
    "TP.HPBITABLO4.1": "TOPLAM YP MEVDUAT (Milyon ABD Dolari)",
    "TP.HPBITABLO4.2": "A. Yurt Ici Yerlesikler (Milyon ABD Dolari)",
    "TP.HPBITABLO4.3": "1. Gercek Kisiler (Milyon ABD Dolari)",
    "TP.HPBITABLO4.4": "a. ABD Dolari (Milyon ABD Dolari)",
    "TP.HPBITABLO4.5": "b. Euro - ABD Dolari Karsiligi (Milyon ABD Dolari)",
    "TP.HPBITABLO4.8": "2. Tuzel Kisiler (Milyon ABD Dolari)",
    "TP.HPBITABLO4.9": "a. ABD Dolari (Milyon ABD Dolari)",
    "TP.HPBITABLO4.13": "B. Yurt Ici Yerlesik Bankalar (Milyon ABD Dolari)",
    "TP.HPBITABLO4.16": "C. Yurt Disi Yerlesikler (Milyon ABD Dolari)",
    "TP.HPBITABLO4.17": "a. ABD Dolari (Milyon ABD Dolari)",
    "TP.HPBITABLO4.18": "b. Euro - ABD Dolari Karsiligi (Milyon ABD Dolari)",
    "TP.HPBITABLO4.21": "D. Yurt Disi Yerlesik Bankalar (Milyon ABD Dolari)",
}


def run_cli(tmp_path, argv):
    out = StringIO()
    err = StringIO()
    code = main(argv, out=out, err=err, cwd=tmp_path)
    return code, out.getvalue(), err.getvalue()


def build_fixture_notebook(tmp_path):
    mapping = {}
    for code in HPBITABLO2_CODES + HPBITABLO3_CODES + HPBITABLO4_CODES:
        if code in {"TP.HPBITABLO4.14", "TP.HPBITABLO4.15"}:
            continue
        normalized = code.replace(".", "_")
        default_unit = "Milyon ABD Dolari" if code.startswith("TP.HPBITABLO4.") else "Bin TL"
        mapping[normalized] = SERIE_NAME_OVERRIDES.get(code, f"Label {normalized} ({default_unit})")

    notebook = {
        "cells": [
            {
                "cell_type": "code",
                "source": ["serie_info"],
                "outputs": [
                    {
                        "output_type": "execute_result",
                        "data": {"text/plain": [repr(mapping)]},
                        "metadata": {},
                        "execution_count": 1,
                    }
                ],
                "metadata": {},
                "execution_count": 1,
            },
            {
                "cell_type": "code",
                "source": [
                    "evds_series_to_get = [\n",
                    f"  {HPBITABLO2_CODES},\n",
                    f"  {HPBITABLO3_CODES},\n",
                    f"  {HPBITABLO4_CODES}\n",
                    "]\n",
                ],
                "outputs": [],
                "metadata": {},
                "execution_count": 2,
            },
            {
                "cell_type": "code",
                "source": ['dth_parite_etkisi = evds.get_data(["TP.HPBITABLO5.12"])\n'],
                "outputs": [],
                "metadata": {},
                "execution_count": 3,
            },
        ],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    notebook_path = tmp_path / "DTH_Blg_V7.ipynb"
    notebook_path.write_text(json.dumps(notebook, ensure_ascii=False), encoding="utf-8")
    return notebook_path


def analysis_by_ticker(result):
    return {item.ticker: item for item in result.analyses}


def test_build_dth_notebook_analysis_extracts_unique_tickers_and_statuses(tmp_path):
    notebook_path = build_fixture_notebook(tmp_path)
    result = build_dth_notebook_analysis(notebook_path)
    items = analysis_by_ticker(result)

    assert len(result.analyses) == 54
    assert result.source_dependencies[0].id == "source:dth-old-series-excel"
    assert items["TP.HPBITABLO3.1"].notebook_status == "listed_only"
    assert items["TP.HPBITABLO3.24"].notebook_status == "listed_only"
    assert items["TP.HPBITABLO4.14"].notebook_status == "fetched_only"
    assert items["TP.HPBITABLO4.15"].notebook_status == "fetched_only"
    assert items["TP.HPBITABLO4.1"].notebook_status == "fetched_only"
    assert items["TP.HPBITABLO4.18"].notebook_status == "fetched_only"
    assert items["TP.HPBITABLO4.2"].notebook_status == "derived_input"
    assert items["TP.HPBITABLO5.12"].notebook_status == "reported_output"


def test_context_titles_are_added_for_ambiguous_series(tmp_path):
    notebook_path = build_fixture_notebook(tmp_path)
    result = build_dth_notebook_analysis(notebook_path)
    items = analysis_by_ticker(result)

    assert items["TP.HPBITABLO2.2"].context_title == "A. TOPLAM MEVDUAT (Bin TL) / 1. Yurt Ici Yerlesikler (Bin TL)"
    assert items["TP.HPBITABLO2.14"].context_title == "A. TOPLAM MEVDUAT (Bin TL) / 2. Yurt Ici Yerlesik Bankalar (Bin TL) / a. TL (Bin TL)"
    assert items["TP.HPBITABLO2.24"].context_title == "B. TOPLAM KREDI (Bin TL) / 1. Yurt Ici Yerlesikler (Bin TL) / a. TL (Bin TL)"
    assert items["TP.HPBITABLO2.33"].context_title == "B. TOPLAM KREDI (Bin TL) / 2. Yurt Ici Yerlesik Finansal Kuruluslar (Bin TL) / a. TL (Bin TL)"
    assert items["TP.HPBITABLO4.4"].context_title == "A. Yurt Ici Yerlesikler (Milyon ABD Dolari) / 1. Gercek Kisiler (Milyon ABD Dolari) / a. ABD Dolari (Milyon ABD Dolari)"
    assert items["TP.HPBITABLO4.17"].context_title == "C. Yurt Disi Yerlesikler (Milyon ABD Dolari) / a. ABD Dolari (Milyon ABD Dolari)"
    assert items["TP.HPBITABLO4.14"].context_title == ""


def test_fix_mojibake_repairs_turkish_series_name():
    clean = "1. Yurt \u0130\u00e7i Yerle\u015fikler (Bin TL)"
    mojibake = clean.encode("utf-8").decode("latin1")
    assert fix_mojibake(mojibake) == clean


def test_extract_unit_ignores_sector_suffixes_and_keeps_real_units():
    assert extract_unit("1. Gercek Kisiler (Milyon ABD Dolari)") == "Milyon ABD Dolari"
    assert extract_unit("Hanehalki (S.14)") == ""
    assert extract_unit("Hanehalki (S.14) (Bankalar Tarafindan Ihrac Edilen)") == ""
    assert extract_unit("USD/TL (Alis Kuru)") == ""


def test_analyze_notebook_generates_report_and_import_csv(tmp_path):
    notebook_path = build_fixture_notebook(tmp_path)

    code, out, err = run_cli(tmp_path, ["analyze-notebook", "--notebook", str(notebook_path), "--spec", "auto"])
    assert code == 0, err
    assert "spec: dth-blg-v7" in out
    assert "tickers: 54" in out

    report_path = tmp_path / "generated" / "DTH_Blg_V7_ticker_report.md"
    import_path = tmp_path / "generated" / "DTH_Blg_V7_registry_import.csv"
    assert report_path.exists()
    assert import_path.exists()

    report = report_path.read_text(encoding="utf-8")
    assert "Baglamli Ad" in report
    assert "## Dis Kaynaklar" in report
    assert "## Source Dependency Eslestirme" in report
    assert "source:dth-old-series-excel" in report
    assert "TP.HPBITABLO4.14" in report

    import_csv = import_path.read_text(encoding="utf-8")
    assert "record_type,id,title,ticker" in import_csv
    assert "source_dependency" in import_csv
    assert "source:dth-old-series-excel" in import_csv

    code, out, err = run_cli(tmp_path, ["import-drafts", "--file", str(import_path)])
    assert code == 0, err
    assert "imported 59 draft(s)" in out


def test_analyze_dth_alias_and_generic_builder_match(tmp_path):
    notebook_path = build_fixture_notebook(tmp_path)
    generic = build_notebook_analysis(notebook_path, spec="dth-blg-v7")
    alias = build_dth_notebook_analysis(notebook_path)

    assert [item.ticker for item in generic.analyses] == [item.ticker for item in alias.analyses]
    assert generic.source_dependencies[0].id == alias.source_dependencies[0].id

    code, out, err = run_cli(tmp_path, ["analyze-dth-notebook", "--notebook", str(notebook_path)])
    assert code == 0, err
    assert "spec: dth-blg-v7" in out
