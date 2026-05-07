"""Fixtures for agent tests."""

from __future__ import annotations

import pandas as pd
import pytest

from evds_registry.agent.tufe_analyst_agent import TUFESnapshot


@pytest.fixture
def mock_tufe_snapshot() -> TUFESnapshot:
    """4 aylık veri içeren mock TUFESnapshot."""
    dates = pd.date_range("2026-02-01", periods=4, freq="MS")
    return TUFESnapshot(
        data=pd.DataFrame(
            {
                "tufe_genel": [100.0, 102.5, 105.0, 107.8],
                "tufe_yillik_pct": [65.0, 62.5, 58.3, 55.1],
                "tufe_aylik_pct": [3.5, 2.5, 2.4, 2.7],
                "cekirdek_b_yillik": [60.0, 58.0, 55.0, 52.0],
                "cekirdek_c_yillik": [58.0, 56.0, 53.0, 50.0],
                "gida_yillik": [80.0, 75.0, 72.0, 70.0],
                "enerji_yillik": [45.0, 42.0, 40.0, 38.0],
                "hizmet_yillik": [55.0, 53.0, 51.0, 49.0],
            },
            index=dates,
        )
    )


@pytest.fixture
def empty_tufe_snapshot() -> TUFESnapshot:
    """Boş veri ile mock TUFESnapshot (null safety testleri için)."""
    return TUFESnapshot(data=pd.DataFrame())
