"""
Step 4: Interactive Dashboard (Streamlit)
- Funnel conversion, top products, revenue trends, KPI summary
Run from project root: streamlit run scripts/dashboard_app.py
Or double-click: run_dashboard.bat
"""
import sys
from pathlib import Path

# Resolve project root and outputs from this script (works even if run from another dir)
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_OUTPUTS = _PROJECT_ROOT / "outputs"
_OUTPUTS.mkdir(parents=True, exist_ok=True)
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="E-Commerce Sales Funnel & Insights", layout="wide")

with st.sidebar:
    st.caption("**How to run**")
    st.code("streamlit run scripts/dashboard_app.py", language=None)
    st.caption("Run from project root. Don't use `python` — the app will close.")
    st.caption(f"**Outputs folder:** `{_OUTPUTS}`")
    st.caption(f"**Exists:** {_OUTPUTS.exists()}")

# Load outputs (run pipeline first)
def load_if_exists(path):
    p = _OUTPUTS / path
    if p.exists():
        try:
            return pd.read_csv(p)
        except Exception:
            return None
    return None

try:
    funnel = load_if_exists("funnel_conversion_rates.csv")
    top_products = load_if_exists("top_products.csv")
    by_category = load_if_exists("revenue_by_category.csv")
    daily = load_if_exists("daily_revenue.csv")
    kpis = load_if_exists("kpis.csv")

    st.title("E-Commerce Sales Funnel & Product Insights")
    st.markdown("Centralized view of conversion, revenue, and product performance.")

    if kpis is not None and len(kpis) > 0:
        row = kpis.iloc[0]
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Revenue", f"${row.get('total_revenue', 0):,.0f}")
        c2.metric("Avg Order Value", f"${row.get('aov', 0):,.2f}")
        c3.metric("Total Orders", f"{int(row.get('total_orders', 0)):,}")
        c4.metric("Repeat Purchaser %", f"{row.get('repeat_purchaser_pct', 0):.1f}%")

    st.subheader("Sales Funnel: Conversion & Drop-off")
    if funnel is not None and len(funnel) > 0:
        col1, col2 = st.columns(2)
        with col1:
            fig = px.bar(
                funnel, x="stage", y="count",
                title="Users at Each Stage",
                labels={"stage": "Stage", "count": "Count"},
                color="count", color_continuous_scale="Blues",
            )
            fig.update_layout(showlegend=False, xaxis_title="", yaxis_title="Count")
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            fig2 = px.bar(
                funnel, x="stage", y="drop_off_from_previous_pct",
                title="Drop-off % from Previous Stage",
                labels={"stage": "Stage", "drop_off_from_previous_pct": "Drop-off %"},
                color="drop_off_from_previous_pct", color_continuous_scale="Reds",
            )
            fig2.update_layout(showlegend=False, xaxis_title="", yaxis_title="Drop-off %")
            st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("Run the pipeline (generate data → clean → funnel → eda) to see funnel charts.")

    st.subheader("Product & Category Performance")
    if top_products is not None and len(top_products) > 0:
        n = st.slider("Top N products", 5, 30, 15)
        top_n = top_products.head(n)
        fig = px.bar(top_n, y="product_name", x="revenue", orientation="h", color="revenue", color_continuous_scale="viridis")
        fig.update_layout(yaxis={"categoryorder": "total ascending"}, height=400, title=f"Top {n} Products by Revenue")
        st.plotly_chart(fig, use_container_width=True)

    if by_category is not None and len(by_category) > 0:
        fig = px.pie(by_category, values="revenue", names="category", title="Revenue Share by Category")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Revenue Over Time")
    if daily is not None and len(daily) > 0:
        daily["date"] = pd.to_datetime(daily["date"])
        fig = px.line(daily, x="date", y="revenue", title="Daily Revenue")
        fig.update_layout(xaxis_title="Date", yaxis_title="Revenue")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Run EDA to populate daily revenue.")

    st.subheader("Recommendations")
    st.markdown("""
- **Highest drop-off stage**: Focus UX and marketing on that stage (e.g. checkout simplification, trust signals).
- **Top products**: Promote best-sellers and bundle underperformers with them.
- **Regional/device segments**: Use funnel_by_*.csv for targeted campaigns.
- **Peak periods**: Align inventory and campaigns with revenue heatmap and daily trend.
""")

except Exception as e:
    st.error("Something went wrong loading the dashboard.")
    st.exception(e)
    st.info("Run the pipeline first from the project folder: `python scripts/run_pipeline.py`")
