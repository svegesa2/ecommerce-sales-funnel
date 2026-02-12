"""
Project configuration: paths and constants for E-Commerce Analytics.
"""
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_CLEANED = PROJECT_ROOT / "data" / "cleaned"
OUTPUTS = PROJECT_ROOT / "outputs"

# Ensure directories exist
DATA_RAW.mkdir(parents=True, exist_ok=True)
DATA_CLEANED.mkdir(parents=True, exist_ok=True)
OUTPUTS.mkdir(parents=True, exist_ok=True)

# Funnel stages (order matters)
FUNNEL_STAGES = ["visit", "signup", "add_to_cart", "purchase"]

# Event type mapping for standardization
EVENT_TYPE_MAP = {
    "visit": "visit",
    "page_view": "visit",
    "signup": "signup",
    "register": "signup",
    "add_to_cart": "add_to_cart",
    "add to cart": "add_to_cart",
    "purchase": "purchase",
    "checkout": "purchase",
    "order": "purchase",
}
