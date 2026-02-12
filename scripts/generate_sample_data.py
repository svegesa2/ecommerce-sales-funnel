"""
Generate synthetic e-commerce data for analysis.
Use this if you don't have Kaggle data yet. Schema matches project requirements.
"""
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta

# Add project root to path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import DATA_RAW

np.random.seed(42)

# --- Parameters --- (reduce for quick demo; increase for full analysis)
N_USERS = 800
N_SESSIONS = 3000
N_PRODUCTS = 100
N_DAYS = 90
START_DATE = datetime(2024, 10, 1)

# Product categories
CATEGORIES = [
    "Electronics", "Clothing", "Home & Garden", "Sports", "Books",
    "Beauty", "Toys", "Food & Beverage"
]

# Regions and devices
REGIONS = ["North", "South", "East", "West", "Central"]
DEVICES = ["mobile", "desktop", "tablet"]
CAMPAIGNS = ["organic", "google", "facebook", "email", "direct"]


def generate_products(n: int) -> pd.DataFrame:
    """Generate product catalog."""
    categories = np.random.choice(CATEGORIES, n)
    prices = np.round(np.random.lognormal(2.5, 1.2, n).clip(5, 500), 2)
    return pd.DataFrame({
        "product_id": [f"P{i:05d}" for i in range(n)],
        "product_name": [f"Product_{i}" for i in range(n)],
        "category": categories,
        "price": prices,
    })


def generate_events(sessions_df: pd.DataFrame, products_df: pd.DataFrame) -> pd.DataFrame:
    """Generate event stream (visit, signup, add_to_cart, purchase)."""
    events = []
    for _, row in sessions_df.iterrows():
        session_id = row["session_id"]
        user_id = row["user_id"]
        ts = row["session_start"]
        device = row["device"]
        region = row["region"]
        campaign = row["campaign_source"]

        # Visit (every session)
        events.append({
            "event_id": f"E{len(events):08d}",
            "session_id": session_id,
            "user_id": user_id,
            "event_type": "visit",
            "product_id": None,
            "quantity": None,
            "timestamp": ts,
            "region": region,
            "device": device,
            "campaign_source": campaign,
        })

        # Signup (subset of sessions - new users)
        if row.get("is_signup", False):
            events.append({
                "event_id": f"E{len(events):08d}",
                "session_id": session_id,
                "user_id": user_id,
                "event_type": "signup",
                "product_id": None,
                "quantity": None,
                "timestamp": ts + timedelta(minutes=np.random.randint(1, 5)),
                "region": region,
                "device": device,
                "campaign_source": campaign,
            })

        # Add to cart (subset)
        if row.get("add_to_cart", False):
            n_items = row.get("cart_items", 1)
            for _ in range(n_items):
                prod = products_df.sample(1).iloc[0]
                events.append({
                    "event_id": f"E{len(events):08d}",
                    "session_id": session_id,
                    "user_id": user_id,
                    "event_type": "add_to_cart",
                    "product_id": prod["product_id"],
                    "quantity": np.random.randint(1, 4),
                    "timestamp": ts + timedelta(minutes=np.random.randint(5, 25)),
                    "region": region,
                    "device": device,
                    "campaign_source": campaign,
                })

        # Purchase (subset of add_to_cart)
        if row.get("purchase", False):
            cart_events = [e for e in events if e["session_id"] == session_id and e["event_type"] == "add_to_cart"]
            for ce in cart_events[: row.get("purchase_items", 1)]:
                events.append({
                    "event_id": f"E{len(events):08d}",
                    "session_id": session_id,
                    "user_id": user_id,
                    "event_type": "purchase",
                    "product_id": ce["product_id"],
                    "quantity": ce["quantity"],
                    "timestamp": ts + timedelta(minutes=np.random.randint(30, 60)),
                    "region": region,
                    "device": device,
                    "campaign_source": campaign,
                })

    return pd.DataFrame(events)


def main():
    products_df = generate_products(N_PRODUCTS)
    products_df.to_csv(DATA_RAW / "products.csv", index=False)
    print(f"Created products: {len(products_df)} rows")

    # Sessions with funnel behavior (realistic drop-offs)
    user_ids = [f"U{i:06d}" for i in range(N_USERS)]
    sessions = []
    for i in range(N_SESSIONS):
        session_start = START_DATE + timedelta(
            days=np.random.randint(0, N_DAYS),
            hours=np.random.randint(0, 24),
            minutes=np.random.randint(0, 60),
        )
        is_signup = np.random.random() < 0.35
        add_to_cart = np.random.random() < 0.45
        purchase = add_to_cart and (np.random.random() < 0.55)
        sessions.append({
            "session_id": f"S{i:08d}",
            "user_id": np.random.choice(user_ids),
            "session_start": session_start,
            "device": np.random.choice(DEVICES, p=[0.5, 0.4, 0.1]),
            "region": np.random.choice(REGIONS),
            "campaign_source": np.random.choice(CAMPAIGNS, p=[0.3, 0.25, 0.2, 0.15, 0.1]),
            "is_signup": is_signup,
            "add_to_cart": add_to_cart,
            "cart_items": np.random.randint(1, 4) if add_to_cart else 0,
            "purchase": purchase,
            "purchase_items": np.random.randint(1, 3) if purchase else 0,
        })

    sessions_df = pd.DataFrame(sessions)
    events_df = generate_events(sessions_df, products_df)

    # Export sessions (for reference) and events
    sessions_df.to_csv(DATA_RAW / "sessions.csv", index=False)
    events_df.to_csv(DATA_RAW / "events.csv", index=False)
    print(f"Created sessions: {len(sessions_df)} rows")
    print(f"Created events: {len(events_df)} rows")
    print(f"Data saved to {DATA_RAW}")


if __name__ == "__main__":
    main()
