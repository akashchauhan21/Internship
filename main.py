"""E-commerce sales analysis project.

This script loads the CSV, does a few basic quality checks, calculates
summary numbers, and saves a small set of charts for the final report.
"""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "sales_data.csv"
OUTPUT_DIR = ROOT / "visualizations"


def load_data(path: Path) -> pd.DataFrame:
    """Load the sales file with a clear error message if something is wrong."""
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    try:
        df = pd.read_csv(path)
    except Exception as exc:  # keeps the script friendly for beginners
        raise ValueError(f"Could not read the CSV file: {exc}") from exc

    if df.empty:
        raise ValueError("The CSV file is empty.")

    return df


def validate_data(df: pd.DataFrame) -> None:
    """Run a few practical checks before doing any analysis."""
    required = {
        "Date",
        "Product",
        "Quantity",
        "Price",
        "Customer_ID",
        "Region",
        "Total_Sales",
    }
    missing_columns = required.difference(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    if df["Date"].isna().any():
        raise ValueError("Date column contains missing values.")

    if df[["Quantity", "Price", "Total_Sales"]].isna().any().any():
        raise ValueError("Sales columns contain missing values.")

    if (df["Quantity"] <= 0).any() or (df["Price"] < 0).any():
        raise ValueError("Quantity must be positive and Price cannot be negative.")

    # This catches accidental changes to Total_Sales before they affect the report.
    calculated_sales = df["Quantity"] * df["Price"]
    if not calculated_sales.equals(df["Total_Sales"]):
        raise ValueError("Total_Sales does not match Quantity * Price for every row.")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Standardise dates and text fields without changing the original data file."""
    clean = df.copy()
    clean["Date"] = pd.to_datetime(clean["Date"], errors="coerce")
    if clean["Date"].isna().any():
        raise ValueError("Some dates could not be converted to a valid date.")

    for column in ["Product", "Customer_ID", "Region"]:
        clean[column] = clean[column].astype(str).str.strip()

    return clean


def make_charts(df: pd.DataFrame) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1) Bar chart: sales by product
    product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
    ax = product_sales.plot(kind="bar", figsize=(9, 5))
    ax.set_title("Total Sales by Product")
    ax.set_xlabel("Product")
    ax.set_ylabel("Sales (₹)")
    ax.tick_params(axis="x", rotation=0)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "product_sales.png", dpi=180)
    plt.close()

    # 2) Line chart: sales over time (monthly)
    monthly_sales = (
        df.set_index("Date")["Total_Sales"]
        .resample("MS")
        .sum()
    )
    ax = monthly_sales.plot(kind="line", marker="o", figsize=(9, 5))
    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales (₹)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_sales.png", dpi=180)
    plt.close()

    # 3) Pie chart: share of sales by region
    region_sales = df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(region_sales.values, labels=region_sales.index, autopct="%1.1f%%", startangle=90)
    ax.set_title("Sales Share by Region")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "region_sales.png", dpi=180)
    plt.close()


def print_summary(df: pd.DataFrame) -> None:
    product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
    region_sales = df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)
    monthly_sales = df.set_index("Date")["Total_Sales"].resample("MS").sum()

    print("\n=== SALES ANALYSIS SUMMARY ===")
    print(f"Date range       : {df['Date'].min().date()} to {df['Date'].max().date()}")
    print(f"Total sales      : ₹{df['Total_Sales'].sum():,.0f}")
    print(f"Units sold       : {df['Quantity'].sum():,}")
    print(f"Average order    : ₹{df['Total_Sales'].mean():,.2f}")
    print(f"Unique customers : {df['Customer_ID'].nunique():,}")
    print(f"Top product      : {product_sales.index[0]} (₹{product_sales.iloc[0]:,.0f})")
    print(f"Top region       : {region_sales.index[0]} (₹{region_sales.iloc[0]:,.0f})")
    print(f"Best month       : {monthly_sales.idxmax().strftime('%B %Y')} (₹{monthly_sales.max():,.0f})")


def main() -> int:
    try:
        df = load_data(DATA_FILE)
        validate_data(df)
        df = clean_data(df)
        make_charts(df)
        print_summary(df)
        print(f"\nCharts saved to: {OUTPUT_DIR}")
        return 0
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
