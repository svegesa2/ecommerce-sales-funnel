# Push to GitHub — Step by Step

Do these in order. Don’t skip steps.

**If you see “git is not recognized”:** Install Git first → see **docs/INSTALL_GIT_WINDOWS.md**, then come back here.

---

## STEP 1 — Create repo on GitHub

1. Open in browser: **https://github.com/new**
2. **Repository name:** type `ecommerce-sales-funnel`
3. **Public** is selected.
4. Leave **README**, **.gitignore**, **license** **unchecked** (we already have them).
5. Click green **Create repository**.
6. Leave the page open; you’ll need the repo URL later.

---

## STEP 2 — Create a Personal Access Token (for password when pushing)

1. Open: **https://github.com/settings/tokens**
2. Click **Generate new token** → **Generate new token (classic)**.
3. **Note:** e.g. `push from PC`
4. **Expiration:** 90 days (or what you prefer).
5. Under **Scopes**, check **repo** (full control of private repositories).
6. Click **Generate token**.
7. **Copy the token** (starts with `ghp_...`) and save it somewhere safe. You’ll paste it when the terminal asks for a password. You won’t see it again.

---

## STEP 3 — Open PowerShell

1. Press **Windows key**, type **PowerShell**, open **Windows PowerShell**.

---

## STEP 4 — Go to your project folder

Type this and press **Enter**:

```powershell
cd c:\Users\veges\OneDrive\Desktop\project
```

Your prompt should show: `PS C:\Users\veges\OneDrive\Desktop\project>`

---

## STEP 5 — Turn the folder into a Git repo and add files

Run these **one at a time** (press Enter after each):

```powershell
git init
```

```powershell
git add .
```

```powershell
git status
```

You should see a list of files. That’s correct.

---

## STEP 6 — First commit

```powershell
git commit -m "E-Commerce Sales Funnel and Product Insights - full project"
```

You should see something like “X files changed”.

---

## STEP 7 — Set branch name to main

```powershell
git branch -M main
```

No output is normal.

---

## STEP 8 — Connect to your GitHub repo

Use your repo name. If you used `ecommerce-sales-funnel` in Step 1, run:

```powershell
git remote add origin https://github.com/svegesa2/ecommerce-sales-funnel.git
```

If you used a **different** repo name, replace `ecommerce-sales-funnel` in the URL with that name.

---

## STEP 9 — Push to GitHub

```powershell
git push -u origin main
```

- A window might open asking you to **sign in to GitHub**. Sign in with your GitHub account.
- If it asks in the **terminal**:
  - **Username:** `svegesa2`
  - **Password:** paste your **Personal Access Token** from Step 2 (you won’t see it as you type — that’s normal).

When it finishes, you should see something like “Branch 'main' set up to track remote branch 'main' from 'origin'.”

---

## STEP 10 — Check on GitHub

1. Open: **https://github.com/svegesa2/ecommerce-sales-funnel**
2. You should see your project files (README, scripts, data, etc.).

Done.

---

## If something goes wrong

- **“remote origin already exists”**  
  Run: `git remote remove origin`  
  Then run again the command from Step 8.

- **“failed to push” / “Authentication failed”**  
  Use the **token** from Step 2 as the password, not your GitHub account password.

- **“repository not found”**  
  Check that the repo name in the URL matches exactly what you created in Step 1, and that you’re logged into the right GitHub account.
