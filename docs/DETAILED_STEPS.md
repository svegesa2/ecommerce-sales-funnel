# E-Commerce Project — Detailed Steps

Follow these steps in order to set up, run, and use the project.

---

## Step 1: Set Up Your Environment

### 1.1 Open the project folder

- Open a terminal (PowerShell or Command Prompt).
- **Always go to the project directory first** — otherwise commands like `python scripts/run_pipeline.py` will fail with "No such file or directory".
  ```powershell
  cd c:\Users\veges\OneDrive\Desktop\project
  ```
  Your prompt should show: `PS C:\Users\veges\OneDrive\Desktop\project>`

### 1.2 Create a virtual environment (recommended)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If you get an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then run the activate command again.

### 1.3 Install dependencies

```powershell
pip install -r requirements.txt
```

This installs: pandas, numpy, matplotlib, seaborn, plotly, streamlit.

---

## Step 2: Generate Sample Data

If you do **not** have your own data yet, generate synthetic data:

```powershell
python scripts/generate_sample_data.py
```

**What this does:**
- Creates `data/raw/products.csv` (product catalog).
- Creates `data/raw/sessions.csv` (session metadata).
- Creates `data/raw/events.csv` (visit, signup, add_to_cart, purchase events).

**Optional:** Edit the top of `scripts/generate_sample_data.py` to change:
- `N_USERS`, `N_SESSIONS`, `N_PRODUCTS`, `N_DAYS` (e.g. more sessions for a larger dataset).

---

## Step 3: Clean the Data

```powershell
python scripts/data_cleaning.py
```

**What this does:**
- Reads from `data/raw/events.csv` and `data/raw/products.csv`.
- Standardizes event types (e.g. "Add to Cart" → "add_to_cart").
- Parses timestamps and drops invalid or duplicate rows.
- Fills missing region/device/campaign with "unknown".
- Writes:
  - `data/cleaned/events_cleaned.csv`
  - `data/cleaned/products_cleaned.csv`
- Saves a short summary to `outputs/cleaning_summary.csv`.

**If you use your own data:** Put your CSVs in `data/raw/` and adjust column names in `scripts/data_cleaning.py` (and in `config.py` for `EVENT_TYPE_MAP` if your event names differ).

---

## Step 4: Run Funnel Analysis

```powershell
python scripts/funnel_analysis.py
```

**What this does:**
- Builds a session-level funnel: Visit → Signup → Add to Cart → Purchase.
- Computes counts and conversion/drop-off rates at each stage.
- Optionally segments by device, region, and campaign source.
- Writes:
  - `outputs/funnel_conversion_rates.csv` — main funnel metrics.
  - `outputs/funnel_counts.csv` — raw counts per stage.
  - `outputs/funnel_by_device.csv`, `funnel_by_region.csv`, `funnel_by_campaign_source.csv` — funnel by segment.

**What to look at:** The stage with the highest **drop-off %** is where to focus UX or marketing improvements.

---

## Step 5: Run Exploratory Data Analysis (EDA)

```powershell
python scripts/eda.py
```

**What this does:**
- Joins purchase events with product data to get revenue per product/category.
- Computes top products, revenue by category, daily revenue, AOV, repeat purchaser %.
- Generates charts and CSVs:
  - `outputs/funnel_chart.png` — funnel bar chart.
  - `outputs/top_products_revenue.png` — top products by revenue.
  - `outputs/revenue_by_category.png` — revenue by category.
  - `outputs/revenue_trend.png` — daily revenue over time.
  - `outputs/revenue_heatmap.png` — revenue by weekday and hour.
  - `outputs/top_products.csv`, `revenue_by_category.csv`, `daily_revenue.csv`, `kpis.csv`.

**What to look at:** Top products to promote, weak categories, seasonal peaks, and KPI trends.

---

## Step 6: Run the Full Pipeline (Optional Shortcut)

Instead of running Steps 2–5 one by one, you can do:

```powershell
python scripts/run_pipeline.py
```

This runs in order: **generate_sample_data.py** → **data_cleaning.py** → **funnel_analysis.py** → **eda.py**. Use this after any change to the sample data or when you want to refresh all outputs.

---

## Step 7: Open the Interactive Dashboard

**Important:** Use **`streamlit run`**, not `python`. If you use `python scripts/dashboard_app.py`, the app will run once and close immediately.

**Easiest:** Double-click **`run_dashboard.bat`** in the project folder (or run it from the terminal). It opens the dashboard and keeps the window open.

**Or run manually:**
```powershell
cd c:\Users\veges\OneDrive\Desktop\project
streamlit run scripts/dashboard_app.py
```

**What this does:**
- Starts a local web server (e.g. http://localhost:8501). Keep the terminal open; closing it will stop the dashboard.
- Opens a dashboard with:
  - KPI cards (Total Revenue, AOV, Total Orders, Repeat Purchaser %).
  - Funnel chart and drop-off chart.
  - Top products by revenue (with a slider for top N).
  - Revenue by category (pie chart).
  - Daily revenue line chart.
  - Short recommendations section.

**Note:** Run the pipeline (Step 6 or Steps 2–5) at least once before opening the dashboard, so the CSV outputs exist.

---

## Step 8: Use the SQL Scripts (If You Have a Database)

If you load your cleaned data into a database (BigQuery, Snowflake, Redshift, etc.):

1. Create tables (or views) for `events_cleaned` and `products_cleaned` that match the column names used in the script.
2. Open `sql/funnel_and_kpis.sql`.
3. Adapt table/schema names to your environment.
4. Run the queries to get:
   - Funnel sessions view.
   - Funnel counts and conversion rates.
   - Funnel by device.
   - Revenue, AOV, order KPIs.
   - Top products by revenue.
   - Daily conversion time series.

---

## Step 9: Read Insights and Recommendations

Open **`docs/INSIGHTS_AND_RECOMMENDATIONS.md`**.

It explains:
- How to interpret funnel and conversion outputs.
- How to use product/category and revenue outputs.
- What to recommend for marketing, product, and UX.
- Optional next steps (forecasting, A/B tests, ETL).

Use this to write your own summary for stakeholders or for your portfolio.

---

## Quick Reference: Command Order

| Order | Command | Purpose |
|-------|--------|--------|
| 1 | `pip install -r requirements.txt` | Install packages |
| 2 | `python scripts/generate_sample_data.py` | Create sample data |
| 3 | `python scripts/data_cleaning.py` | Clean data |
| 4 | `python scripts/funnel_analysis.py` | Funnel analysis |
| 5 | `python scripts/eda.py` | EDA and charts |
| 6 | `streamlit run scripts/dashboard_app.py` | Open dashboard |

**Or:** After Step 1, run `python scripts/run_pipeline.py` (covers 2–5), then run the Streamlit command (6).

---

## Where Everything Is Saved

| Output | Location |
|--------|----------|
| Raw data | `data/raw/*.csv` |
| Cleaned data | `data/cleaned/*.csv` |
| Funnel & EDA CSVs | `outputs/*.csv` |
| Charts | `outputs/*.png` |
| SQL | `sql/funnel_and_kpis.sql` |
| Docs | `docs/` (this file, INSIGHTS_AND_RECOMMENDATIONS.md) |

---

## Troubleshooting

- **"No module named 'config'"** — Run commands from the project root: `c:\Users\veges\OneDrive\Desktop\project`.
- **Dashboard shows "Run the pipeline..."** — Run `python scripts/run_pipeline.py` (or Steps 2–5) first.
- **Script not found** — Ensure you are in the project folder and use `python scripts/script_name.py`.
- **PowerShell: "cannot be loaded because running scripts is disabled"** — Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` (see Step 1.2).
