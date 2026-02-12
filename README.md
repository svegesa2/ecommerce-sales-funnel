# E-Commerce Sales Funnel & Product Insights

[![Live Dashboard](https://img.shields.io/badge/📊_Live_Dashboard-View_here-FF4B4B?style=for-the-badge&logo=streamlit)](https://ecommerce-sales-funnel.streamlit.app/)

**→ [View live interactive dashboard](https://ecommerce-sales-funnel.streamlit.app/)** *(replace with your deployed link after deployment)*

---

A portfolio-ready **data analytics project** for a mid-sized e-commerce company. It provides a centralized view of the sales funnel, product performance, and customer behavior to support marketing, product strategy, and UX decisions.

---

## 1. Business Problem

The company collects large volumes of **user clickstream, purchase, and product data** but lacks a centralized view. Goals:

- **Increase sales conversion** across the website  
- **Identify top-selling and underperforming products**  
- **Understand customer behavior** (e.g. drop-offs in checkout, seasonal purchase trends)  

This project delivers cleaned data, funnel analysis, EDA, visualizations, and an interactive dashboard with **actionable recommendations**.

---

## 2. Project Objectives

- Analyze the **sales funnel**: Visit → Signup → Add to Cart → Purchase  
- Identify **drop-off points** and **conversion rates** at each stage  
- Perform **EDA** on product sales: top products, categories, revenue trends  
- Build **dashboards** to communicate insights to stakeholders  
- Suggest **actionable recommendations** for marketing, product, and UX  

---

## 3. Dataset

### Option A: Synthetic data (included)

The repo includes a **sample data generator** so you can run the project without external data:

- **Events**: `event_type` (visit, signup, add_to_cart, purchase), `session_id`, `user_id`, `product_id`, `quantity`, `timestamp`, `region`, `device`, `campaign_source`
- **Products**: `product_id`, `product_name`, `category`, `price`

### Option B: Kaggle / external data

Use datasets such as:

- **E-Commerce Customer Behavior** or **Online Retail Dataset** on Kaggle  

Ensure your data has (or can be mapped to):

- User ID, Session ID, Event Type (Visit, Add to Cart, Purchase)  
- Product ID, Category, Price, Quantity  
- Timestamp / Date  
- Optional: Region, Device, Campaign Source  

Place raw CSVs in `data/raw/` and align column names in `scripts/data_cleaning.py` if needed.

---

## 4. Tools & Skills

| Tool / Skill | Use in this project |
|--------------|----------------------|
| **Python** (pandas, NumPy, Matplotlib, Seaborn, Plotly) | Data cleaning, EDA, visualizations |
| **SQL** | Funnel aggregation, KPIs (see `sql/funnel_and_kpis.sql`) |
| **Streamlit** | Interactive dashboard |
| **Excel / PivotTables** | Optional for ad-hoc analysis on exported CSVs |

---

## 5. Step-by-Step Methodology

| Step | Description | Script / Asset |
|------|-------------|----------------|
| **1. Data cleaning** | Handle missing values, duplicates, timestamps; standardize event types, categories, regions | `scripts/data_cleaning.py` |
| **2. Funnel analysis** | Count users at each stage; conversion and drop-off rates; optional segmentation by device, region, campaign | `scripts/funnel_analysis.py`, `sql/funnel_and_kpis.sql` |
| **3. EDA** | Top products/categories, daily revenue, seasonality heatmap, AOV, repeat rate | `scripts/eda.py` |
| **4. Dashboard** | Funnel chart, top products, revenue by category, daily trend, KPI summary | `scripts/dashboard_app.py` (Streamlit) |
| **5. Insights & recommendations** | Documented in `docs/INSIGHTS_AND_RECOMMENDATIONS.md` | — |

---

## 6. Repository Structure

```
project/
├── config.py                 # Paths and constants
├── requirements.txt
├── README.md
├── data/
│   ├── raw/                  # Raw CSVs (events, products, sessions)
│   └── cleaned/              # Cleaned datasets
├── outputs/                  # Funnel CSVs, EDA results, charts
├── scripts/
│   ├── generate_sample_data.py
│   ├── data_cleaning.py
│   ├── funnel_analysis.py
│   ├── eda.py
│   ├── dashboard_app.py
│   └── run_pipeline.py
├── sql/
│   └── funnel_and_kpis.sql   # Funnel & KPI queries (adapt to your DB)
└── docs/
    └── INSIGHTS_AND_RECOMMENDATIONS.md
```

---

## 7. How to Run

**For a full step-by-step walkthrough**, see **[docs/DETAILED_STEPS.md](docs/DETAILED_STEPS.md)**.

### Prerequisites

- Python 3.9+
- pip

### Setup

```bash
cd project
pip install -r requirements.txt
```

### Full pipeline (synthetic data)

```bash
python scripts/run_pipeline.py
```

This will:

1. Generate sample data in `data/raw/`
2. Clean and write to `data/cleaned/`
3. Run funnel analysis and write CSVs to `outputs/`
4. Run EDA and save charts to `outputs/`

### Run steps individually

```bash
python scripts/generate_sample_data.py
python scripts/data_cleaning.py
python scripts/funnel_analysis.py
python scripts/eda.py
```

### Interactive dashboard

```bash
streamlit run scripts/dashboard_app.py
```

Open the URL shown in the terminal (e.g. http://localhost:8501).

### SQL

Use `sql/funnel_and_kpis.sql` in your data warehouse (BigQuery, Snowflake, Redshift, etc.). Adapt table and column names to your schema.

---

## 8. Make the Dashboard Visible to Recruiters / Hiring Managers

To give hiring managers a **one-click link** to your dashboard (instead of only local run instructions):

1. **Deploy the app** on **[Streamlit Community Cloud](https://share.streamlit.io)** (free):
   - Push this repo to your GitHub.
   - Go to [share.streamlit.io](https://share.streamlit.io), sign in with GitHub.
   - Click **“New app”**, select this repository.
   - Set **Main file path** to: `scripts/dashboard_app.py`.
   - Deploy. You’ll get a URL like: `https://your-repo-name.streamlit.app`.

2. **Add the link to the README** so it’s the first thing they see:
   - Replace `https://YOUR-APP-NAME.streamlit.app` at the top of this README with your real URL.
   - The badge and “View live interactive dashboard” link will then point to your live app.

3. **Ensure the dashboard has data**: Run the pipeline once (e.g. locally), then commit the `outputs/` folder so the deployed app can read the CSVs, *or* run the pipeline as part of deployment (e.g. in a GitHub Action that generates `outputs/` and Streamlit reads from the repo). For the simplest approach, commit the contents of `outputs/` so the cloud app has something to show.

**Full deployment steps:** [docs/DEPLOY.md](docs/DEPLOY.md)

---

## 9. Deliverables Summary

| Deliverable | Location |
|-------------|----------|
| Cleaned dataset | `data/cleaned/` |
| Python scripts (cleaning, funnel, EDA) | `scripts/` |
| SQL for funnel & KPIs | `sql/funnel_and_kpis.sql` |
| Interactive dashboard | `scripts/dashboard_app.py` (Streamlit) |
| Methodology & insights | This README + `docs/INSIGHTS_AND_RECOMMENDATIONS.md` |

---

## 10. Optional Extensions

- **Predictive analytics**: Forecast sales by product/region (e.g. Prophet, ARIMA).  
- **A/B testing**: Analyze experiments for campaigns or landing pages.  
- **ETL pipeline**: Automate nightly refresh and re-run of cleaning, funnel, and EDA.

---

## 11. License

MIT License — see [LICENSE](LICENSE). Use freely for learning and portfolio purposes.

---

## 12. Before Pushing to GitHub

See **[docs/BEFORE_PUSH_CHECKLIST.md](docs/BEFORE_PUSH_CHECKLIST.md)** for a short checklist and push commands.
