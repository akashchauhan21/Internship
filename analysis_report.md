# Sales Analysis Report

## 1. Project overview

This project uses the provided `sales_data.csv` file to perform a small but complete sales analysis. The workflow starts with data validation, followed by cleaning, basic calculations, visualisation, and a short written summary.

The main purpose is not just to produce charts. It is to check whether the data is reliable enough to analyse and then explain what the numbers actually show.

## 2. Data quality check

The dataset contains 100 rows and 7 columns:

- Date
- Product
- Quantity
- Price
- Customer_ID
- Region
- Total_Sales

There are no missing values in the provided dataset.

A second check compares `Quantity × Price` against `Total_Sales` for every row. The values match throughout the dataset, so no correction to the sales totals was needed.

## 3. Key numbers

| Metric | Result |
|---|---:|
| Total sales | ₹1,23,65,048 |
| Units sold | 478 |
| Average sales per row | ₹1,23,650.48 |
| Unique customers | 100 |
| Date range | Jan 1, 2024 – Apr 9, 2024 |

## 4. Sales by product

| Product | Orders | Units | Sales |
|---|---:|---:|---:|
| Laptop | 24 | 136 | ₹38,89,210 |
| Tablet | 26 | 127 | ₹28,84,340 |
| Phone | 20 | 101 | ₹28,59,394 |
| Headphones | 15 | 48 | ₹13,84,033 |
| Monitor | 15 | 66 | ₹13,48,071 |

### What stands out

Laptop sales are the largest in the dataset at **₹38.89 lakh**. They also have the highest unit volume at 136 units.

Tablet and Phone sales are quite close to each other, both sitting around ₹28–29 lakh. Headphones and Monitor are much lower in total sales than the other three products.

The chart makes the gap between the product groups easier to see than the table alone.

![Sales by product](../visualizations/product_sales.png)

## 5. Monthly sales trend

| Month | Orders | Units | Sales |
|---|---:|---:|---:|
| January 2024 | 31 | 147 | ₹41,20,524 |
| February 2024 | 29 | 112 | ₹26,56,050 |
| March 2024 | 31 | 175 | ₹44,85,006 |
| April 2024* | 9 | 44 | ₹11,03,468 |

\* April only contains data through April 9, 2024.

### What stands out

Sales dip in February and then rise sharply in March. March is the strongest month in this dataset, with **₹44,85,006** in sales and 175 units sold.

April appears much lower, but this is mainly because the dataset stops on April 9. Comparing that partial month directly with complete months would be misleading.

![Monthly sales trend](../visualizations/monthly_sales.png)

## 6. Sales by region

| Region | Orders | Units | Sales |
|---|---:|---:|---:|
| North | 28 | 147 | ₹39,83,635 |
| South | 27 | 143 | ₹37,37,852 |
| East | 19 | 94 | ₹25,19,639 |
| West | 26 | 94 | ₹21,23,922 |

### What stands out

North contributes the highest sales at about **₹39.84 lakh**, followed closely by South at about **₹37.38 lakh**.

East and West both sold 94 units, but East generated more sales than West. That suggests the value of individual orders is not identical across regions.

![Sales share by region](../visualizations/region_sales.png)

## 7. Final insights

A few practical points come out of the analysis:

1. **Laptop is the strongest product in this dataset.** It leads both total sales and units sold.
2. **March is the strongest month**, while February shows a noticeable dip before the March increase.
3. **North and South together make up a large share of sales**, so these two regions are important contributors in the sample.
4. **April needs to be treated carefully** because it is only a partial month.
5. The raw dataset is internally consistent, which makes it a good base for this analysis exercise.

## 8. Limitations

This is a relatively small dataset with 100 sales records and only a little more than three months of dates. It does not include product profit, discounts, returns, marketing spend, or customer demographics.

Because of that, the analysis can describe what happened in this dataset, but it should not be used to make strong business forecasts on its own.

## 9. Tools used

- Python
- pandas
- Matplotlib
- pytest
- GitHub for project versioning and presentation
