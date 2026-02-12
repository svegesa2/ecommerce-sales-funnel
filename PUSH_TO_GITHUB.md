# Push This Project to Your GitHub (svegesa2)

Follow these steps **in order**. You must do Step 1 on GitHub in your browser; the rest is in PowerShell from the project folder.

---

## Step 1: Create the repo on GitHub

1. Go to **https://github.com/new**
2. **Repository name:** `ecommerce-sales-funnel` (or any name you like)
3. **Description (optional):** `E-Commerce Sales Funnel & Product Insights - Data Analytics`
4. Choose **Public**
5. **Do not** check "Add a README" (you already have one)
6. Click **Create repository**

---

## Step 2: Open PowerShell in the project folder

```powershell
cd c:\Users\veges\OneDrive\Desktop\project
```

---

## Step 3: Initialize git and push (first time only)

Run these commands **one by one**. Replace `ecommerce-sales-funnel` with your repo name if you used a different one.

```powershell
git init
git add .
git status
git commit -m "E-Commerce Sales Funnel & Product Insights - full project"
git branch -M main
git remote add origin https://github.com/svegesa2/ecommerce-sales-funnel.git
git push -u origin main
```

When you run `git push`, GitHub will ask you to **sign in**:
- Use your GitHub username: **svegesa2**
- For password, use a **Personal Access Token** (GitHub no longer accepts account passwords for push).
  - Create one: GitHub → Settings → Developer settings → Personal access tokens → Generate new token (classic). Give it `repo` scope, copy the token, and paste it when prompted as the password.

---

## Step 4: After first push (later updates)

When you change files and want to push again:

```powershell
cd c:\Users\veges\OneDrive\Desktop\project
git add .
git commit -m "Your short message"
git push
```

---

## Repo URL

After pushing, your project will be at:
**https://github.com/svegesa2/ecommerce-sales-funnel**

(Change `ecommerce-sales-funnel` if you used a different repo name.)
