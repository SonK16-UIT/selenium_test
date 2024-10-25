import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Send 'chrome' or 'firefox' as parameter for execution"
    )

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    options = Options()
    options.add_argument('--head')
    driver = None

    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.implicitly_wait(10)
    yield driver
    driver.quit()
