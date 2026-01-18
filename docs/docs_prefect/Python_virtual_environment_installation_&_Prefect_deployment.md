# Python Virtual Environment & Prefect Deployment
---
## **Query 01:**  I have this folder created inside 001_venv_prefect: `venv_prefect` update the commands accordingly, and help me understand which directory is the virtual environment: `001_venv_prefect` or inner folder `venv_prefect` ?
---

**Let’s clear it up cleanly and update the commands exactly for your setup.**

**📁 Your current folder structure:**
```
001_venv_prefect/
 └── venv_prefect/
     ├── Scripts/
     ├── Lib/
     ├── pyvenv.cfg
```
---
**❓ Which directory is the virtual environment?**

*✅ **venv_prefect** is the virtual environment*

It contains:
- Scripts\python.exe
- Scripts\activate
- Lib\site-packages
- pyvenv.cfg

*❌ 001_venv_prefect is NOT the virtual environment*

- It is your project root
- It holds the virtual environment folder
  
---
**📌 Rule to remember**

The folder that contains **Scripts / Lib / pyvenv.cfg** is the virtual environment.

---

**✅ PowerShell commands for YOUR setup:**

1️⃣ Navigate to project root: `cd 001_venv_prefect`

2️⃣ Activate the virtual environment: `.\venv_prefect\Scripts\Activate.ps1`

You should see: *(venv_prefect) PS C:\...\001_venv_prefect>*

6️⃣ Deactivate the environment: `deactivate`

**🔁 If you ever need to recreate the venv from inside `001_venv_prefect:`**
```powershell
Remove-Item -Recurse -Force venv_prefect
python -m venv venv_prefect
.\venv_prefect\Scripts\Activate.ps1
```
---
**🧠 Mental model (important)**

Think of it like this:

| Folder / Path            | Purpose                          |
|--------------------------|----------------------------------|
| `001_venv_prefect`       | Project workspace                |
| `venv_prefect`           | Isolated Python runtime          |
| `Scripts\python.exe`     | Python used when venv is active  |
| `Lib\site-packages`      | Installed libraries              |

---
**⚠️ Best practice tip**

**Never:**
- edit files inside venv_prefect
- commit venv_prefect to Git

**Instead:**
- keep code in 001_venv_prefect
- recreate venv from requirements.txt
  
---
## **Query 02:**  I have modules installed in virtual environment, let me know how can I create a `requirement.txt` so that I can install them to reuse in another environment?
---

**Got it — both points are common on PowerShell + Windows. Let’s handle them clearly and practically.**

**1️⃣ Why where python returned nothing:**

✔️ What’s happening

In PowerShell, `where` is NOT reliable for commands unless they’re traditional executables on PATH.

PowerShell’s native command is: `Get-Command python`

**Expected output (when venv is active):**

| CommandType  | Name   | Source                                                       |
|--------------|--------|--------------------------------------------------------------|
| Application  | python | `...\001_venv_prefect\venv_prefect\Scripts\python.exe`       |
|


---
**Double-check using Python itself:**
`python -c "import sys; print(sys.executable)"`

---
**2️⃣ Create requirements.txt from installed modules:**

You already have modules installed in `venv_prefect`.  Here’s how to capture them correctly.

✅ Step 1: Activate the virtual environment: 

`cd 001_venv_prefect`

`.\venv_prefect\Scripts\Activate.ps1`

✅ Step 2: Generate requirements.txt (BEST method):

`pip freeze > requirements.txt`


This creates:  **001_venv_prefect\requirements.txt**

Example contents:
```
prefect==2.14.5
requests==2.31.0
pandas==2.1.4
```

- ✔ This file is portable
- ✔ This is standard practice
- ✔ This is what you should share or commit
---
🔍 Optional: View installed packages before freezing: `pip list` or exact freeze format preview: `pip list --format=freeze`

---
**3️⃣ Install these modules in another environment on another machine or venv:**
```powershell
python -m venv venv_prefect
.\venv_prefect\Scripts\Activate.ps1
pip install -r requirements.txt
```

---
**🧠 Important best-practice notes**

❌ Don’t do this
- Copy venv_prefect folder
- Manually list packages
- Use system Python

✅ Always do this
- Use pip freeze
- Store requirements.txt at project root
- Recreate venv when needed

**🔑 Mental model (keep this)**

- Virtual env = Python + site-packages
- requirements.txt = recipe to rebuild it

---
---
## **Query 03:**  I want to create a prefect flow and run it in my local system, by creating local deployment server, both through powershell and prefect UI. Keep in mind all the command should be for latest prefect 3. Prefect Flow File name: prefect_sample_001.py
---

**1. Activate virtual environment (recommended)**

Activate the virtual environment: `.\venv_prefect\Scripts\Activate.ps1`

Verify: `prefect --version`

Expected (example):
```
Version: 3.x.x
```
---

**2. Start a Local Prefect Server (UI + API)**

Prefect 3 uses a local orchestration server (not Prefect Cloud).

**2.1 Start the server: `prefect server start`**

What happens:
- API starts on: http://127.0.0.1:4200/api
- UI starts on: http://127.0.0.1:4200

**👉 Keep this terminal running**

**Terminal 01:**

![Terminal 01](../attachments/Python_virtual_environment_installation_%26_Prefect_deployment_001.jpg)


---
**3. Configure Prefect to Use the Local Server**

3.1 Open a new PowerShell window

3.2 Activate the virtual environment: `.\venv_prefect\Scripts\Activate.ps1`

3.3 Configure prefect: `prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api`


3.4 Verify: `prefect config view`

**Terminal 02:**

![Terminal 02](../attachments/Python_virtual_environment_installation_%26_Prefect_deployment_002.jpg)

---
**4. Run the Flow Directly (Local Execution – No Deployment)**

This is useful for quick testing: `python prefect_sample_001.py`


You will see:
- Tasks running in parallel
- Logs appearing in the terminal
- Flow run visible in Prefect UI → Flow Runs

---
**5. Create a Local Deployment (Required for UI-triggered runs)**

Deployments allow:
- Running from UI
- Scheduling
- Parameter overrides

**5.1 Create deployment from the directory containing prefect_sample_001.py:**

- prefect_sample_001.py → file name
- prefect_sample_001_parallel → flow function
- default → built-in local pool

**Open another PowerShell window:**

Step 1: Create a local process work pool: `prefect work-pool create default --type process`

Expected output:

`Created work pool 'default-agent-pool'`

Step 2: Verify work pool exists: `prefect work-pool ls`


You should see:

`default   process`

Step 3: Start a worker for that pool: `prefect worker start --pool default`


**👉 Keep this terminal running**

**Terminal 03:**

![Terminal 03](../attachments/Python_virtual_environment_installation_%26_Prefect_deployment_003.jpg)

---

**Step 4: Re-run deployment (safe to re-run)**
To re-run for this deployment, use the following command:

`prefect deployment run 'prefect_sample_001_parallel/local-parallel-deployment'`

- Open UI, browser:  http://127.0.0.1:4200


**Prefect Run UI:**

![Prefect Run UI](../attachments/Python_virtual_environment_installation_%26_Prefect_deployment_Prefect_Run.jpg)

---