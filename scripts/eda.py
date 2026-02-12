"""
Step 3: Exploratory Data Analysis
- Top products and categories, revenue trends, seasonality
- Average order value, total revenue, repeat purchases
"""
import pandas as pd
import numpy as np
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import DATA_CLEANED, OUTPUTS

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", palette="muted")
OUTPUTS.mkdir(parents=True, exist_ok=True)


def load_data():
    events = pd.read_csv(DATA_CLEANED / "events_cleaned.csv")
    products = pd.read_csv(DATA_CLEANED / "products_cleaned.csv")
    events["timestamp"] = pd.to_datetime(events["timestamp"])
    return events, products


def merge_purchases_with_products(events: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    purchases = events[events["event_type"] == "purchase"].copy()
    purchases = purchases.merge(products[["product_id", "product_name", "category", "price"]], on="product_id", how="left")
    purchases["revenue"] = purchases["quantity"] * purchases["price"]
    return purchases


def top_products_and_categories(purchases: pd.DataFrame):
    by_product = (
        purchases.groupby(["product_id", "product_name", "category"])
        .agg(units_sold=("quantity", "sum"), revenue=("revenue", "sum"))
        .reset_index()
        .sort_values("revenue", ascending=False)
    )
    by_category = (
        purchases.groupby("category")
        .agg(units_sold=("quantity", "sum"), revenue=("revenue", "sum"), orders=("session_id", "nunique"))
        .reset_index()
        .sort_values("revenue", ascending=False)
    )
    return by_product, by_category


def revenue_trends(purchases: pd.DataFrame) -> pd.DataFrame:
    purchases["date"] = purchases["timestamp"].dt.date
    daily = purchases.groupby("date").agg(
        revenue=("revenue", "sum"),
        orders=("session_id", "nunique"),
        units=("quantity", "sum"),
    ).reset_index()
    daily["date"] = pd.to_datetime(daily["date"])
    return daily


def aov_and_repeat(events: pd.DataFrame, purchases: pd.DataFrame) -> dict:
    orders_per_session = purchases.groupby("session_id")["revenue"].sum()
    aov = float(orders_per_session.mean())
    total_revenue = float(orders_per_session.sum())
    repeat = events[events["event_type"] == "purchase"].groupby("user_id")["session_id"].nunique()
    repeat_pct = (repeat > 1).mean() * 100 if len(repeat) else 0
    return {"aov": aov, "total_revenue": total_revenue, "repeat_purchaser_pct": repeat_pct, "total_orders": len(orders_per_session)}


def plot_funnel_chart():
    """Bar chart of funnel conversion (uses funnel output if present)."""
    fp = OUTPUTS / "funnel_conversion_rates.csv"
    if not fp.exists():
        return
    df = pd.read_csv(fp)
    fig, ax = plt.subplots(figsize=(8, 5))
    x = range(len(df))
    ax.bar(x, df["count"], color=sns.color_palette("Blues_d", len(df))[::-1], edgecolor="white")
    ax.set_xticks(x)
    ax.set_xticklabels(df["stage"].str.replace("_", " ").str.title())
    ax.set_ylabel("Count")
    ax.set_title("Sales Funnel: Users at Each Stage")
    for i, (_, row) in enumerate(df.iterrows()):
        ax.annotate(f"{row['conversion_from_visit_pct']:.1f}%", (i, row["count"]), ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    plt.savefig(OUTPUTS / "funnel_chart.png", dpi=150, bbox_inches="tight")
    plt.close()


def plot_top_products(by_product: pd.DataFrame, top_n: int = 15):
    df = by_product.head(top_n)
    fig, ax = plt.subplots(figsize=(10, 6))
    y_pos = range(len(df))
    ax.barh(y_pos, df["revenue"], color=sns.color_palette("viridis", len(df)))
    ax.set_yticks(y_pos)
    ax.set_yticklabels(df["product_name"].str[:30], fontsize=9)
    ax.invert_yaxis()
    ax.set_xlabel("Revenue")
    ax.set_title(f"Top {top_n} Products by Revenue")
    plt.tight_layout()
    plt.savefig(OUTPUTS / "top_products_revenue.png", dpi=150, bbox_inches="tight")
    plt.close()


def plot_top_categories(by_category: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=by_category, x="revenue", y="category", palette="rocket", ax=ax)
    ax.set_xlabel("Revenue")
    ax.set_ylabel("Category")
    ax.set_title("Revenue by Category")
    plt.tight_layout()
    plt.savefig(OUTPUTS / "revenue_by_category.png", dpi=150, bbox_inches="tight")
    plt.close()


def plot_revenue_trend(daily: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(daily["date"], daily["revenue"], color="steelblue", linewidth=1.5)
    ax.fill_between(daily["date"], daily["revenue"], alpha=0.3)
    ax.set_xlabel("Date")
    ax.set_ylabel("Revenue")
    ax.set_title("Daily Revenue Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUTPUTS / "revenue_trend.png", dpi=150, bbox_inches="tight")
    plt.close()


def plot_heatmap_seasonality(purchases: pd.DataFrame):
    purchases["weekday"] = purchases["timestamp"].dt.dayofweek
    purchases["hour"] = purchases["timestamp"].dt.hour
    cross = purchases.groupby(["weekday", "hour"])["revenue"].sum().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(12, 4))
    sns.heatmap(cross, cmap="YlOrRd", ax=ax, cbar_kws={"label": "Revenue"})
    ax.set_xticklabels([f"{h}h" for h in range(24)])
    ax.set_yticklabels(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    ax.set_title("Revenue by Weekday & Hour (Heatmap)")
    plt.tight_layout()
    plt.savefig(OUTPUTS / "revenue_heatmap.png", dpi=150, bbox_inches="tight")
    plt.close()


def main():
    print("Loading data...")
    events, products = load_data()
    purchases = merge_purchases_with_products(events, products)

    print("Top products and categories...")
    by_product, by_category = top_products_and_categories(purchases)
    by_product.to_csv(OUTPUTS / "top_products.csv", index=False)
    by_category.to_csv(OUTPUTS / "revenue_by_category.csv", index=False)

    print("Revenue trends...")
    daily = revenue_trends(purchases)
    daily.to_csv(OUTPUTS / "daily_revenue.csv", index=False)

    kpis = aov_and_repeat(events, purchases)
    pd.DataFrame([kpis]).to_csv(OUTPUTS / "kpis.csv", index=False)
    print("KPIs:", kpis)

    print("Generating plots...")
    plot_funnel_chart()
    plot_top_products(by_product)
    plot_top_categories(by_category)
    plot_revenue_trend(daily)
    plot_heatmap_seasonality(purchases)

    print(f"EDA outputs and charts saved to {OUTPUTS}")


if __name__ == "__main__":
    main()
