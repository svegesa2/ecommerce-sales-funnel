"""
Step 2: Funnel Analysis
- Count users/sessions at each stage: Visit -> Signup -> Add to Cart -> Purchase
- Conversion and drop-off rates; optional segmentation (device, region, campaign)
"""
import pandas as pd
import numpy as np
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import DATA_CLEANED, FUNNEL_STAGES, OUTPUTS


def load_cleaned_data():
    events = pd.read_csv(DATA_CLEANED / "events_cleaned.csv")
    events["timestamp"] = pd.to_datetime(events["timestamp"])
    return events


def funnel_by_session(events: pd.DataFrame) -> pd.DataFrame:
    """One row per session: whether it reached each stage (1/0)."""
    sessions = events.groupby("session_id").agg(
        visit=("event_type", lambda x: (x == "visit").any().astype(int)),
        signup=("event_type", lambda x: (x == "signup").any().astype(int)),
        add_to_cart=("event_type", lambda x: (x == "add_to_cart").any().astype(int)),
        purchase=("event_type", lambda x: (x == "purchase").any().astype(int)),
    ).reset_index()
    return sessions


def funnel_counts(sessions: pd.DataFrame) -> pd.DataFrame:
    """Cumulative counts: each stage counts only if previous stages done (ordered funnel)."""
    counts = []
    for i, stage in enumerate(FUNNEL_STAGES):
        if i == 0:
            n = sessions[stage].sum()
        else:
            prev_stages = FUNNEL_STAGES[: i + 1]
            n = sessions[sessions[prev_stages].min(axis=1) == 1][stage].sum()
        counts.append({"stage": stage, "count": int(n)})
    return pd.DataFrame(counts)


def conversion_rates(counts_df: pd.DataFrame) -> pd.DataFrame:
    """Conversion rate from first stage (visit) and stage-to-stage."""
    counts = counts_df["count"].values
    result = []
    for i, stage in enumerate(FUNNEL_STAGES):
        from_visit = counts[i] / counts[0] * 100 if counts[0] else 0
        from_prev = counts[i] / counts[i - 1] * 100 if i > 0 and counts[i - 1] else (100 if i == 0 else 0)
        result.append({
            "stage": stage,
            "count": counts[i],
            "conversion_from_visit_pct": round(from_visit, 2),
            "conversion_from_previous_stage_pct": round(from_prev, 2),
            "drop_off_from_previous_pct": round(100 - from_prev, 2) if i > 0 else 0,
        })
    return pd.DataFrame(result)


def funnel_by_segment(events: pd.DataFrame, segment_col: str) -> pd.DataFrame:
    """Funnel counts and conversion by segment (e.g. device, region)."""
    sessions = funnel_by_session(events)
    segment = events.groupby("session_id")[segment_col].first()
    sessions = sessions.merge(segment, left_on="session_id", right_index=True)

    rows = []
    for seg_val, grp in sessions.groupby(segment_col):
        counts_df = funnel_counts(grp)
        conv = conversion_rates(counts_df)
        conv[segment_col] = seg_val
        rows.append(conv)
    return pd.concat(rows, ignore_index=True)


def main():
    print("Loading cleaned events...")
    events = load_cleaned_data()

    sessions = funnel_by_session(events)
    counts_df = funnel_counts(sessions)
    funnel_rates = conversion_rates(counts_df)

    funnel_rates.to_csv(OUTPUTS / "funnel_conversion_rates.csv", index=False)
    counts_df.to_csv(OUTPUTS / "funnel_counts.csv", index=False)
    print("Funnel conversion rates:")
    print(funnel_rates.to_string(index=False))

    for seg_col in ["device", "region", "campaign_source"]:
        if seg_col in events.columns:
            seg_funnel = funnel_by_segment(events, seg_col)
            seg_funnel.to_csv(OUTPUTS / f"funnel_by_{seg_col}.csv", index=False)
            print(f"Funnel by {seg_col} saved.")

    print(f"\nOutputs saved to {OUTPUTS}")


if __name__ == "__main__":
    main()
