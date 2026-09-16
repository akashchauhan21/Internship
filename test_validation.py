"""Small validation checks for the project dataset."""

from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from main import load_data, validate_data  # noqa: E402


DATA_FILE = ROOT / "data" / "sales_data.csv"


def test_file_loads():
    df = load_data(DATA_FILE)
    assert len(df) == 100
    assert df.shape[1] == 7


def test_no_missing_values():
    df = load_data(DATA_FILE)
    assert int(df.isna().sum().sum()) == 0


def test_sales_calculation_matches():
    df = load_data(DATA_FILE)
    validate_data(df)
    pd.testing.assert_series_equal(
        df["Quantity"] * df["Price"],
        df["Total_Sales"],
        check_names=False,
    )
