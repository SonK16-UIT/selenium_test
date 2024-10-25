from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, by_type, identifier, timeout=10):
    """Wait for an element to be located."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by_type, identifier))
    )

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        """Opens the login page."""
        self.driver.get(url)

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
        """
        Verifies if the login was successful by checking if the dashboard link is displayed.
        Returns True if successful, False otherwise.
        """
        try:
            # Wait until the DASHBOARD link text is present and visible
            dashboard_text = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'DASHBOARD')]"))
            )
            return dashboard_text.is_displayed()
        except Exception:
            return False  # Return False if the element is not found or times out
