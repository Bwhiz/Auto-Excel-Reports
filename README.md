# Auto-Excel-Reports

This repository contains scripts and workflows to automate the generation and distribution of Excel reports using Python's `openpyxl` library. The automation is achieved using GitHub Actions, enabling scheduled and event-triggered report generation and email distribution.

## Features
- **Automated Report Generation:** Uses `openpyxl` to create and format Excel reports.
- **Scheduled Execution:** GitHub Actions workflow to run the scripts daily or on push events.
- **Email Distribution:** Automatically sends the generated reports via email using SMTP.
- **Environment Variables for Configuration:** Securely handles sensitive information like email credentials using GitHub Secrets.
- **Customizable Workflows:** Easily modify the schedule and triggers as per your requirements.

## Usage
1. **Set Up GitHub Secrets:** Store your email credentials and other sensitive information in the GitHub Secrets.
2. **Configure Workflow:** Customize the GitHub Actions workflow file to set the schedule and other configurations.
3. **Run Scripts:** On push to the main branch or on the defined schedule, the scripts will generate the reports and send them via email.

## Getting Started
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Auto-Excel-Reports.git
   cd Auto-Excel-Reports

2. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt

3. **Set up environment variables:** 
- Add necessary environment variables to your GitHub Secrets.

4. **Modify scripts as needed:** 
- Customize the Python scripts for your specific reporting requirements.

## Example Workflow

```yaml
name: Daily House Report Script Execution

on:
  push:
    branches:
      - main
  schedule:
    - cron: '0 0 * * *'

jobs:
  run-scripts:
    runs-on: ubuntu-latest

    env:
      sheet_name: ${{ secrets.SHEET_NAME }}
      sheet_id: ${{ secrets.SHEET_ID }}
      app_password: ${{ secrets.APP_PASSWORD }}
      sender_email: ${{ secrets.SENDER_EMAIL }}
      recipient_mail: ${{ secrets.RECIPIENT_MAIL }}

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

    - name: Run Report Script
      run: python report_script.py

