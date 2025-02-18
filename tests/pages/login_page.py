# tests/pages/login_page.py
from tests.utils.selenium_utils import wait_for_element
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        """Opens the login page."""
        self.driver.get("https://home-automation-raspi.firebaseapp.com/login")

    def enter_username(self, username):
        """Fills in the username."""
        self.driver.find_element(By.ID, "email").send_keys(username)

    def enter_password(self, password):
        """Fills in the password."""
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        """Clicks the login button."""
        self.driver.find_element(By.ID, "login_button").click()

    def verify_successful_login(self):
        """Verifies if the login was successful by checking for the dashboard."""
        try:
            dashboard_text = wait_for_element(
                self.driver,
                By.XPATH,
                "//h2[contains(text(), 'DASHBOARD')]",
                timeout=5
            )
            return dashboard_text.is_displayed()
        except Exception:
            return False
