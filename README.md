### 🚀 Data Engineering CI/CD Practice Lab

A streamlined Python data collection utility built to practice local environment management, database integration, and automated CI/CD deployment pipelines. 

### 🛠️ The Tech Stack

* **Language:** Python 3.12
* **Database:** SQLite3 (Embedded Serverless DB)
* **Code Formatting:** Black Formatter
* **Automation:** GitHub Actions (Ubuntu Runner)

### 🏗️ Project Architecture & Workflow

text

[Local Machine]                                 [GitHub Cloud]
   ├── Python Script (main.py)                    └── GitHub Actions CI Pipeline
   ├── SQLite Database (users.db)                      ├── Setup Python Environment
   └── Local Black Formatting Check                    ├── Dependency Installation
                                                       └── Automated Code Formatting Check (Black)

Use code with caution.

1. **Data Intake:** main.py provisions a local database infrastructure dynamically on-demand and captures structured demographic user datasets.
2. **Local Validation:** Codebase isolation managed using Python native virtual environments (venv) with structural linting enforced by black.
3. **Automated Pipeline:** Every codebase adjustment pushed to the main branch automatically provisions a headless Ubuntu workflow environment via GitHub Actions to validate file styling health.

### ⚡ Quick Start Guide

### 1. Initialize the Environment

Clone the repository, initialize your virtual environment execution pipeline, and clear PowerShell execution restrictions: 

powershell

# Clone and enter directory
cd cicd_practice

# Initialize & activate environment
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\Activate.ps1

Use code with caution.

### 2. Install Pipeline Packages

Deploy required production linting tools locally: 

powershell

pip install -r requirements.txt

Use code with caution.

### 3. Run the Core Application

Execute the ingestion script to dynamically spin up the database layer and feed data: 

powershell

python main.py

Use code with caution.

### 🤖 CI/CD Integration Details

This project includes automated quality control using .github/workflows/ci.yml. On every push or pull_request to the main branch, GitHub Actions: 

* Spins up an ubuntu-latest virtual machine.
* Configures isolated Python 3.12 binaries.
* Installs requirements from requirements.txt.
* Executes black --check . to enforce clean coding standards before allowing a merge.