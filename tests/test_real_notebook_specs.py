from __future__ import annotations

from io import StringIO
from pathlib import Path

import pytest

from evds_registry.cli import main
from evds_registry.notebook_analysis import build_notebook_analysis


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_ROOT = REPO_ROOT.parent / "Telegram Bot" / "notebooks"


def run_cli(tmp_path: Path, argv: list[str]) -> tuple[int, str, str]:
    out = StringIO()
    err = StringIO()
    code = main(argv, out=out, err=err, cwd=tmp_path)
    return code, out.getvalue(), err.getvalue()


@pytest.mark.skipif(not NOTEBOOK_ROOT.exists(), reason="Notebook fixtures are not available in this environment.")
@pytest.mark.parametrize(
    ("filename", "expected_tickers", "expected_source_dependencies"),
    [
        ("DTH_Blg_V7.ipynb", 54, 1),
        ("Eurobnd_Blg_V4.ipynb", 10, 3),
        ("PrBnk_MnklKymt_V5.ipynb", 57, 2),
        ("Pys_Ktlmclr_V2.ipynb", 14, 0),
        ("Rzrv_Blg_V7.ipynb", 10, 2),
        ("Tbl_Apko.ipynb", 40, 4),
        ("Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb", 84, 3),
    ],
)
def test_real_notebook_specs_generate_report_and_import(tmp_path, filename, expected_tickers, expected_source_dependencies):
    notebook_path = NOTEBOOK_ROOT / filename
    result = build_notebook_analysis(notebook_path, spec="auto")

    assert len(result.analyses) == expected_tickers
    assert len(result.source_dependencies) == expected_source_dependencies

    code, out, err = run_cli(tmp_path, ["analyze-notebook", "--notebook", str(notebook_path), "--spec", "auto"])
    assert code == 0, err
    assert f"tickers: {expected_tickers}" in out

    report_path = tmp_path / "generated" / f"{notebook_path.stem}_ticker_report.md"
    import_path = tmp_path / "generated" / f"{notebook_path.stem}_registry_import.csv"
    assert report_path.exists()
    assert import_path.exists()

    report = report_path.read_text(encoding="utf-8")
    assert "## Dis Kaynaklar" in report
    assert "## Tam Ticker Eslestirme" in report
    assert "## Source Dependency Eslestirme" in report
    assert "## Belirsizlikler" in report

    code, out, err = run_cli(tmp_path, ["import-drafts", "--file", str(import_path)])
    assert code == 0, err
    assert "imported" in out


@pytest.mark.skipif(not NOTEBOOK_ROOT.exists(), reason="Notebook fixtures are not available in this environment.")
def test_yi_real_person_fx_securities_are_weekly_million_usd():
    notebook_path = NOTEBOOK_ROOT / "Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb"
    result = build_notebook_analysis(notebook_path, spec="auto")
    items = {item.ticker: item for item in result.analyses}

    expected = {
        "TP.EBONDPIYDEG.S14": "Eurobond (Gercek Kisi)",
        "TP.YDOSBAPIYDEG.S15": "Ozel Sektor Eurobond (Gercek Kisi)",
        "TP.YDOSBAPIYDEG.S34": "Ozel Sektor Eurobond (Gercek Kisi)",
        "TP.YDOSBAPIYDEG.S53": "Ozel Sektor Eurobond (Gercek Kisi)",
        "TP.YDOSBAPIYDEG.S72": "Ozel Sektor Eurobond (Gercek Kisi)",
    }

    for ticker, note_fragment in expected.items():
        item = items[ticker]
        assert item.frequency == "weekly"
        assert item.unit == "Milyon ABD Dolari"
        assert note_fragment in item.notes
