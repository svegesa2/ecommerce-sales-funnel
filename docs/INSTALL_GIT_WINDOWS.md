# Install Git on Windows (so you can push to GitHub)

If PowerShell says **"git is not recognized"**, install Git first, then do the push steps.

---

## Step 1: Download Git for Windows

1. Open: **https://git-scm.com/download/win**
2. The download should start automatically (e.g. **64-bit Git for Windows Setup**).
3. If it doesn’t, click the download link for your Windows (64-bit or 32-bit).

---

## Step 2: Run the installer

1. Open the downloaded file (e.g. `Git-2.43.0-64-bit.exe`).
2. Click **Next** through the screens. Default options are fine.
3. On **"Adjusting your PATH environment"**:
   - Choose **"Git from the command line and also from 3rd-party software"** (recommended).
4. Keep other defaults and click **Next** until **Install**, then **Finish**.

---

## Step 3: Use a new PowerShell window

1. **Close** your current PowerShell window.
2. Open a **new** PowerShell (Windows key → type **PowerShell** → Enter).
3. Check that Git works:
   ```powershell
   git --version
   ```
   You should see something like `git version 2.43.0.windows.1`.

---

## Step 4: Push your project

1. Go to your project folder:
   ```powershell
   cd c:\Users\veges\OneDrive\Desktop\project
   ```
2. Continue from **STEP 5** in **STEP_BY_STEP_PUSH.md** (git init, add, commit, remote, push).

---

## If `git` is still not recognized

- Restart your PC after installing Git, then try again.
- Or use **Git Bash** (installed with Git): open **Git Bash** from the Start menu and run the same commands there.
