# Selenium WebDriver Configuration for Pytest with Browser Selection

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


# Add command-line option for browser selection
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Select 'chrome' or 'firefox' for execution"
    )

# Fixture to initialize WebDriver based on selected browser
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    options = Options()
    #options.add_argument('--headless')

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# To run:
# pytest --browser=chrome or pytest --browser=firefox
