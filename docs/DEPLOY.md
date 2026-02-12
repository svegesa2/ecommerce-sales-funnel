# Deploy Dashboard So Hiring Managers Can See It

Deploying the Streamlit app gives you a **public link** you can put in your README, resume, or LinkedIn so recruiters and hiring managers can open the dashboard without cloning the repo.

---

## Option: Streamlit Community Cloud (free, recommended)

### 1. Prepare the repo

- Push the project to GitHub (if you haven’t already).
- **Important:** The dashboard reads from the `outputs/` folder (CSV files). So either:
  - **A)** Run the pipeline locally once, then **commit the `outputs/` folder** and push. The deployed app will use these files from the repo.
  - **B)** Or leave `outputs/` out of the repo; the app will still open but will show “Run the pipeline…” messages until data is present. For a strong impression, use **A**.

### 2. Deploy on Streamlit Community Cloud

1. Go to **[share.streamlit.io](https://share.streamlit.io)**.
2. Sign in with your **GitHub** account.
3. Click **“New app”**.
4. Choose:
   - **Repository:** your GitHub username / this repo name.
   - **Branch:** `main` (or your default branch).
   - **Main file path:** `scripts/dashboard_app.py`.
5. Click **“Deploy!”**.
6. Wait a few minutes. You’ll get a URL like:
   - `https://your-repo-name.streamlit.app`

### 3. Make the link visible on GitHub

1. Open your **README.md** in the repo.
2. At the top you’ll see:
   - A badge and a line like: **→ View live interactive dashboard (replace with your deployed link after deployment)**.
3. Replace `https://YOUR-APP-NAME.streamlit.app` with your **real** URL (e.g. `https://ecommerce-funnel.streamlit.app`).
4. Commit and push.

Now anyone opening your repo (including hiring managers) will see the **Live Dashboard** badge and link at the very top.

### 4. Use the link elsewhere

- **Resume / portfolio:** Add the same URL under “Projects” or “Live demos”.
- **LinkedIn:** Put it in the project description or in a “Featured” link.
- **Cover letter:** “You can try the interactive dashboard here: [link].”

---

## If the deployed app shows “Run the pipeline…”

The app needs the files in `outputs/` (e.g. `funnel_conversion_rates.csv`, `top_products.csv`, `kpis.csv`). On Streamlit Cloud the app runs from your repo; it does **not** run your pipeline. So:

- Run locally: `python scripts/run_pipeline.py`
- Commit the new/updated files under `outputs/` and push.
- Redeploy or wait for Streamlit to redeploy from the latest commit.

After that, the live link will show the same charts and KPIs as on your machine.

---

## Summary

| Step | Action |
|------|--------|
| 1 | Run pipeline locally; commit and push `outputs/` (recommended). |
| 2 | Deploy at [share.streamlit.io](https://share.streamlit.io) with Main file path: `scripts/dashboard_app.py`. |
| 3 | Copy the app URL and put it in the README (replace `YOUR-APP-NAME.streamlit.app`). |
| 4 | Use that same URL on resume, LinkedIn, or in applications so the link is visible to hiring managers. |
