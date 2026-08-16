# SQL Sales Dashboard

A retail sales analysis project using **SQL (SQLite)**, **Python**, and **Excel**,
designed to feed directly into a **Power BI** dashboard.

## Project Structure

```
sql-sales-dashboard/
├── data/
│   └── generate_data.py     # creates data/sales.db with synthetic sales
├── sql/
│   └── queries.sql          # raw SQL queries, for reference
├── src/
│   ├── db.py                 # SQLite connection helper
│   ├── queries.py            # named queries used by the report
│   └── report.py             # runs queries, exports to Excel
├── main.py
├── requirements.txt
└── outputs/
    └── sales_report.xlsx     # generated multi-sheet Excel report
```

## Setup

```bash
pip install -r requirements.txt
python main.py
```

This creates `data/sales.db` (a SQLite database with a `sales` table) and
`outputs/sales_report.xlsx`, a workbook with one sheet per query:

- `revenue_by_category`
- `revenue_by_store`
- `monthly_trend`
- `top_products`
- `store_category_breakdown`

## Building the Power BI Dashboard

1. Open **Power BI Desktop** → **Get Data**.
2. Choose either:
   - **Excel workbook** → select `outputs/sales_report.xlsx`, or
   - **SQLite database** (via ODBC driver) → select `data/sales.db` directly.
3. Load the tables and build visuals, for example:
   - Bar chart: `revenue_by_category`
   - Line chart: `monthly_trend`
   - Map/column chart: `revenue_by_store`
   - Table: `top_products`
   - Stacked bar: `store_category_breakdown`
4. Add slicers for `store` and `category` to make the dashboard interactive.

## License

MIT
