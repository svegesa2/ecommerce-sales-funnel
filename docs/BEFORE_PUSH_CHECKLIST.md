# Before You Push to GitHub

Quick checklist so your repo looks good to recruiters and reviewers.

---

## Required (you’re already set)

- [x] **README.md** — Project overview, how to run, deliverables
- [x] **requirements.txt** — All Python dependencies
- [x] **.gitignore** — Python, venv, IDE, OS junk
- [x] **Documentation** — DETAILED_STEPS.md, INSIGHTS_AND_RECOMMENDATIONS.md
- [x] **LICENSE** — MIT (or replace with your choice)

---

## Recommended (do once)

1. **Run the full pipeline locally**
   ```powershell
   pip install -r requirements.txt
   python scripts/run_pipeline.py
   streamlit run scripts/dashboard_app.py
   ```
   Confirm there are no errors and the dashboard loads.

2. **Decide what to commit**
   - **Commit sample data** (`data/raw/*.csv`) — OK if small; lets others run without generating.
   - **Commit sample outputs** (`outputs/*.csv`, `outputs/*.png`) — Optional; shows results in the repo. If you prefer a lean repo, add `outputs/` to `.gitignore` and don’t commit them.

---

## Optional polish

- Add a **screenshot** of the dashboard to the README (e.g. “Dashboard preview”).
- In README, add your **Kaggle/dataset link** if you switch from synthetic data.
- **Pin Python version** in README (e.g. “Python 3.9+”).

---

## Push commands

```powershell
cd c:\Users\veges\OneDrive\Desktop\project
git init
git add .
git commit -m "E-Commerce Sales Funnel & Product Insights - full project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your GitHub repo.

---

You’re good to push once the pipeline runs successfully on your machine.
