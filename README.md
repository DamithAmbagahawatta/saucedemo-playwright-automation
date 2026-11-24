pip install playwright
pip install pytest
pip install pytest-playwright
pip install pytest-html
pip install allure-pytest
pip install python-dotenv   



1.python -m playwright install
2.python -m playwright install chromium
3.python -m playwright install-deps  


8. Automation Project එක Run කරන්න
Command	Purpose
pytest	සියලුම test run කරනවා
pytest -v	Detailed test results
pytest -s	Print statements පෙන්වනවා
pytest -v -s	Detailed + print
pytest --headed	Browser එක visible කරලා run කරනවා
pytest --browser chromium	Chromium browser එකෙන් run කරනවා  

  

python -m playwright install chromium




















# SauceDemo Automation Testing Project

## Project Overview

This project is a Web Automation Testing project developed using:

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Allure Report

The main purpose of this project is to automate web application testing using Playwright and Pytest.

**Application Under Test:** https://www.saucedemo.com/

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Playwright | Browser Automation |
| Pytest | Test Framework |
| POM | Test Code Organization |
| Allure | Test Reporting |
| VS Code | Code Editor |

---

## Project Structure

```text
Automation_test/
│
├── .venv/
│
├── pages/
│   ├── __init__.py
│   └── saucedemo.py
│
├── test/
│   └── test_saucedemo.py
│
├── reports/
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Installation Guide

### 1. Clone or Open Project

Open the project folder in VS Code.

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate Virtual Environment

Ubuntu / Linux:

```bash
source .venv/bin/activate
```

### 4. Install Required Packages

```bash
pip install -r requirements.txt
```

### 5. Install Playwright Browsers

```bash
python -m playwright install chromium
```

### 6. Install Browser Dependencies (Ubuntu)

```bash
sudo python -m playwright install-deps chromium
```

---

## Running Tests

### Run All Tests

```bash
pytest
```

### Run Tests with Detailed Output

```bash
pytest -v -s
```

### Run Tests with Visible Browser

```bash
pytest -v -s --headed
```

### Run Tests Using Chromium

```bash
pytest --browser chromium
```

---

## Allure Report

### Execute Tests and Generate Allure Results

```bash
pytest --alluredir=reports/allure-results
```

### Generate Allure HTML Report

```bash
allure generate reports/allure-results -o reports/allure-report --clean
```

### Open Allure Report

```bash
allure open reports/allure-report
```

---

## Test Automation Workflow

1. Start Pytest.
2. Pytest initializes the Playwright browser fixture.
3. Browser page is passed to the test function.
4. Page Object Model class is initialized.
5. Page methods perform browser actions.
6. Pytest validates test results.
7. Allure generates test reports.

---

## Page Object Model (POM)

This project follows the Page Object Model design pattern.

**Benefits:**

- Code reusability
- Easy maintenance
- Better code organization
- Separation of test logic and page actions
- Easy debugging

---

## Test Scenarios

| Test ID | Test Scenario | Status |
|---|---|---|
| TC_001 | Open SauceDemo Website | Planned |
| TC_002 | Verify Login Functionality | Planned |
| TC_003 | Verify Product List | Planned |
| TC_004 | Add Product to Cart | Planned |
| TC_005 | Remove Product from Cart | Planned |
| TC_006 | Complete Checkout | Planned |

---

## Author

QA Automation Project

**Automation Framework:** Python + Playwright + Pytest
# saucedemo-playwright-automation
