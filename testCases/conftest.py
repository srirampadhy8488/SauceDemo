import pytest
from selenium import webdriver
from datetime import datetime
import os
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
def pytest_addoption(parser): # This will get the value from the CLI/hooks
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose browser: chrome, edge, or firefox")


@pytest.fixture()
def browser(request):  # This will return the browser value to the setup method
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        ops = ChromeOptions()
        # 1. Disable the password manager and breach popups
        ops.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })

        # 2. Disable the "Automation" info-bar
        # This is the correct way to handle experimental options
        ops.add_experimental_option("excludeSwitches", ["enable-automation"])

        # 3. Add arguments to ensure the browser stays clean and fast
        ops.add_argument("--disable-notifications")
        ops.add_argument("--incognito")  # This is your best defense against popups

        driver = webdriver.Chrome(options=ops)
        print("\n--- Launching Chrome Browser ---")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("\n--- Launching Edge Browser ---")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("\n--- Launching Firefox Browser ---")
    else:
        # If an invalid browser is passed, default to Chrome
        driver = webdriver.Chrome()
        print("\n--- Browser not recognized. Defaulting to Chrome ---")
    return driver
########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'SauceDemo'
    config._metadata['Module Name'] = 'Login Page'
    config._metadata['Tester'] = 'Sriram'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"