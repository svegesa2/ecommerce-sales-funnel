# E-Commerce Sales Funnel & Product Insights

[![Live Dashboard](https://img.shields.io/badge/📊_Live_Dashboard-View_here-FF4B4B?style=for-the-badge&logo=streamlit)](https://ecommerce-sales-funnel.streamlit.app/)

<<<<<<< HEAD
**→ [View live interactive dashboard](https://YOUR-APP-NAME.streamlit.app)**
=======
**→ [View live interactive dashboard](https://ecommerce-sales-funnel.streamlit.app/)** 
>>>>>>> be2e47e307c96aabdb8dbea3fb3a817d9465fd40

---

A **data analytics project** for a mid-sized e-commerce company. It provides a centralized view of the sales funnel, product performance, and customer behavior to support marketing, product strategy, and UX decisions.

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

- **Events:** `event_type` (visit, signup, add_to_cart, purchase), `session_id`, `user_id`, `product_id`, `quantity`, `timestamp`, `region`, `device`, `campaign_source`
- **Products:** `product_id`, `product_name`, `category`, `price`

Synthetic data can be generated with `scripts/generate_sample_data.py`. For Kaggle or external data, place raw CSVs in `data/raw/` and align column names in `scripts/data_cleaning.py` if needed.

---

## 4. Tools & Skills

| Tool / Skill | Use in this project |
|--------------|----------------------|
| **Python** (pandas, NumPy, Matplotlib, Seaborn, Plotly) | Data cleaning, EDA, visualizations |
| **SQL** | Funnel aggregation, KPIs (`sql/funnel_and_kpis.sql`) |
| **Streamlit** | Interactive dashboard |

---

## 5. Methodology

| Step | Description | Script / Asset |
|------|-------------|----------------|
| **1. Data cleaning** | Handle missing values, duplicates, timestamps; standardize event types, categories, regions | `scripts/data_cleaning.py` |
| **2. Funnel analysis** | Count users at each stage; conversion and drop-off rates; segmentation by device, region, campaign | `scripts/funnel_analysis.py`, `sql/funnel_and_kpis.sql` |
| **3. EDA** | Top products/categories, daily revenue, seasonality heatmap, AOV, repeat rate | `scripts/eda.py` |
| **4. Dashboard** | Funnel chart, top products, revenue by category, daily trend, KPI summary | `scripts/dashboard_app.py` (Streamlit) |
| **5. Insights & recommendations** | Documented in `docs/INSIGHTS_AND_RECOMMENDATIONS.md` | — |

---

## 6. Repository Structure

```
project/
├── config.py
├── requirements.txt
├── README.md
├── data/
│   ├── raw/
│   └── cleaned/
├── outputs/
├── scripts/
│   ├── generate_sample_data.py
│   ├── data_cleaning.py
│   ├── funnel_analysis.py
│   ├── eda.py
│   ├── dashboard_app.py
│   └── run_pipeline.py
├── sql/
│   └── funnel_and_kpis.sql
└── docs/
    ├── INSIGHTS_AND_RECOMMENDATIONS.md
    └── RESUME_PROJECT_BLOCK.md
```

---

## 7. Deliverables

| Deliverable | Location |
|-------------|----------|
| Cleaned dataset | `data/cleaned/` |
| Python scripts (cleaning, funnel, EDA) | `scripts/` |
| SQL for funnel & KPIs | `sql/funnel_and_kpis.sql` |
| Interactive dashboard | `scripts/dashboard_app.py` (Streamlit) |
| Insights & recommendations | `docs/INSIGHTS_AND_RECOMMENDATIONS.md` |

---

## 8. License

MIT License — see [LICENSE](LICENSE).
