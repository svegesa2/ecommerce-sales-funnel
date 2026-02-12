"""
Step 1: Data Cleaning
- Handle missing values, duplicates, incorrect timestamps
- Standardize event types, product categories, regions
"""
import pandas as pd
import numpy as np
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import DATA_RAW, DATA_CLEANED, EVENT_TYPE_MAP, OUTPUTS


def load_raw_data():
    """Load raw CSVs. Adapt column names if using Kaggle dataset."""
    events = pd.read_csv(DATA_RAW / "events.csv")
    products = pd.read_csv(DATA_RAW / "products.csv")
    return events, products


def clean_events(events: pd.DataFrame) -> pd.DataFrame:
    # Standardize event_type
    if "event_type" in events.columns:
        events["event_type"] = (
            events["event_type"]
            .str.strip()
            .str.lower()
            .replace(EVENT_TYPE_MAP)
        )
        # Drop unmapped / invalid event types
        valid = ["visit", "signup", "add_to_cart", "purchase"]
        events = events[events["event_type"].isin(valid)]

    # Parse timestamp
    ts_col = "timestamp" if "timestamp" in events.columns else "event_time"
    if ts_col in events.columns:
        events[ts_col] = pd.to_datetime(events[ts_col], errors="coerce")
        events = events.dropna(subset=[ts_col])
        # Remove future or very old dates (sanity check)
        events = events[
            (events[ts_col] >= "2020-01-01") & (events[ts_col] <= pd.Timestamp.now() + pd.Timedelta(days=1))
        ]

    # Drop full duplicates
    events = events.drop_duplicates()

    # Fill optional columns with defaults
    for col in ["region", "device", "campaign_source"]:
        if col in events.columns:
            events[col] = events[col].fillna("unknown").astype(str).str.strip()
        else:
            events[col] = "unknown"

    if "quantity" in events.columns:
        events["quantity"] = pd.to_numeric(events["quantity"], errors="coerce").fillna(1).astype(int)
    return events


def clean_products(products: pd.DataFrame) -> pd.DataFrame:
    # Standardize category
    if "category" in products.columns:
        products["category"] = products["category"].fillna("Uncategorized").str.strip()

    # Price: non-negative, numeric
    if "price" in products.columns:
        products["price"] = pd.to_numeric(products["price"], errors="coerce")
        products = products[products["price"].notna() & (products["price"] >= 0)]

    return products.drop_duplicates(subset=["product_id"] if "product_id" in products.columns else None)


def main():
    print("Loading raw data...")
    events, products = load_raw_data()

    print("Cleaning events...")
    events_clean = clean_events(events)
    print("Cleaning products...")
    products_clean = clean_products(products)

    events_clean.to_csv(DATA_CLEANED / "events_cleaned.csv", index=False)
    products_clean.to_csv(DATA_CLEANED / "products_cleaned.csv", index=False)

    print(f"Events: {len(events)} -> {len(events_clean)}")
    print(f"Products: {len(products)} -> {len(products_clean)}")
    print(f"Cleaned data saved to {DATA_CLEANED}")

    # Summary report
    report = {
        "events_rows": len(events_clean),
        "products_rows": len(products_clean),
        "event_types": events_clean["event_type"].value_counts().to_dict(),
    }
    pd.DataFrame([report]).to_csv(OUTPUTS / "cleaning_summary.csv", index=False)
    print("Cleaning summary saved to outputs/cleaning_summary.csv")


if __name__ == "__main__":
    main()
