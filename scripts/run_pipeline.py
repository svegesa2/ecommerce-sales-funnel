"""
Run full pipeline: generate sample data -> clean -> funnel -> EDA.
Execute from project root: python scripts/run_pipeline.py
"""
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

def run(script: str, name: str) -> bool:
    print(f"\n--- {name} ---")
    r = subprocess.run([sys.executable, str(PROJECT_ROOT / "scripts" / script)], cwd=PROJECT_ROOT)
    return r.returncode == 0

def main():
    steps = [
        ("generate_sample_data.py", "Generate sample data"),
        ("data_cleaning.py", "Data cleaning"),
        ("funnel_analysis.py", "Funnel analysis"),
        ("eda.py", "EDA & visualizations"),
    ]
    for script, name in steps:
        if not run(script, name):
            print(f"Pipeline failed at: {name}")
            sys.exit(1)
    print("\nPipeline complete. Run dashboard with: streamlit run scripts/dashboard_app.py")

if __name__ == "__main__":
    main()
