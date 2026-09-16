# E-commerce Sales Analysis

A small end-to-end data analysis project built with Python. The goal is simple: take a raw sales CSV, check that the data makes sense, find a few useful patterns, and turn those numbers into charts that are easy to understand.

## Project goal

This project looks at sales by **product**, **region**, and **month**. I wanted the analysis to answer a few practical questions:

- Which products bring in the most sales?
- Which region contributes the most revenue?
- How do sales move from month to month?
- Are the totals in the dataset internally consistent?

## Dataset

File: `data/sales_data.csv`

- 100 rows
- 7 columns
- Date range: January 1, 2024 to April 9, 2024
- Products: Laptop, Tablet, Phone, Headphones, Monitor
- Regions: North, South, East, West

The dataset has no missing values. `Total_Sales` also matches `Quantity × Price` across all rows, so the report uses the original sales values after validation.

## Folder structure

```text
sales_analysis_project/
│
├── data/
│   └── sales_data.csv
│
├── report/
│   └── analysis_report.md
│
├── tests/
│   └── test_validation.py
│
├── visualizations/
│   ├── product_sales.png
│   ├── monthly_sales.png
│   └── region_sales.png
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd sales_analysis_project
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the analysis

```bash
python main.py
```

The script prints the main numbers in the terminal and saves three charts inside `visualizations/`.

### 5. Run the tests

```bash
pytest -q
```

## What the analysis found

The dataset contains total sales of **₹1,23,65,048** across **478 units** and **100 customers**. The **Laptop** category contributes the largest amount of sales, while **North** is the highest-sales region.

Monthly sales are strongest in **March 2024**, with January next. April is lower, but it only contains data through April 9, so it should not be treated as a full-month comparison.

The full numbers and chart-based observations are in `report/analysis_report.md`.

## Technical approach

The project follows a basic analysis pipeline:

1. **Load** — read the CSV with pandas.
2. **Validate** — check required columns, missing values, positive quantities, valid prices, and the `Quantity × Price = Total_Sales` rule.
3. **Clean** — convert dates to datetime and trim text fields.
4. **Analyze** — group sales by product and region and resample sales by month.
5. **Visualize** — create bar, line, and pie charts with Matplotlib.
6. **Report** — explain the numbers in plain language.
7. **Test** — run simple automated checks with pytest.

## Error handling

The script gives readable errors when the CSV is missing, empty, has required columns missing, contains invalid dates, has invalid sales values, or contains inconsistent `Total_Sales` values.

## Screenshots / visual documentation

The three PNG files inside `visualizations/` are the visual documentation for the project and can also be embedded directly in a GitHub README later.

## Notes

This is a learning project, so the focus is on clean fundamentals rather than making the charts overly complicated. The idea is to make the analysis understandable first and fancy second.
