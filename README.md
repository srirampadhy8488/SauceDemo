# Selenium Python Automation Framework – SauceDemo

This project demonstrates automated testing of the **SauceDemo web application** using **Selenium WebDriver with Python and PyTest**.
The framework follows the **Page Object Model (POM)** design pattern to maintain clean, reusable, and scalable test automation code.

---

## Tools & Technologies

* Python
* Selenium WebDriver
* PyTest
* Page Object Model (POM)
* Data Driven Testing (Excel)
* Logging
* PyTest Fixtures

---

## Framework Features

* Page Object Model design pattern
* Data-driven testing using Excel
* PyTest based test execution
* Centralized configuration management
* Logging support for debugging
* Screenshot capture on test failure
* Organized folder structure for scalability

---

## Project Structure

```
SauceDemo
│
├── configurations
│   └── config.ini
│
├── logs
│   └── automation.log
│
├── pageObjects
│   ├── LoginPage.py
│   └── ProductPage.py
│
├── reports
│
├── screenshots
│   └── test_productpage.png
│
├── testCases
│   ├── conftest.py
│   ├── test_login.py
│   └── test_login_data_driven.py
│
├── testData
│   └── LoginData.xlsx
│
├── utilities
│   ├── customLogger.py
│   ├── ExcelUtils.py
│   └── readProperties.py
│
├── requirements.txt
└── main.py
```

---

## Automated Test Scenarios

Currently automated scenarios include:

* Login with valid credentials
* Login validation
* Data-driven login testing using Excel
* Product page validation

Additional scenarios such as **cart and checkout flows** can be extended easily due to the modular framework design.

---

## Website Under Test

https://www.saucedemo.com

---

## How to Run the Tests

### 1. Clone the repository

```
git clone https://github.com/srirampadhy8488/SauceDemo.git
```

### 2. Navigate to the project folder

```
cd SauceDemo
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run tests using PyTest

```
pytest
```

---

## Author

**Sriram Padhy**

QA Engineer transitioning into **Automation Testing with Selenium and Python**.
