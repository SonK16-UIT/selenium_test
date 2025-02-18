from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils.selenium_utils import wait_for_element  # Import shared utility

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        """Simulates the logout process."""
        # Click on the dropdown (assuming this opens the logout menu)
        dropdown_button = wait_for_element(
            self.driver, By.CSS_SELECTOR, '[data-testid="ArrowDropDownOutlinedIcon"]', timeout=5
        )
        dropdown_button.click()

        # Wait for the "Log Out" button to appear and click it
        logout_button = wait_for_element(
            self.driver, By.XPATH, "//li[contains(text(), 'Log Out')]", timeout=5
        )
        logout_button.click()

    def verify_successful_logout(self):
        """
        Verifies if the logout was successful by checking if the login button is displayed.
        Returns True if successful, False otherwise.
        """
        try:
            login_button = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, "login_button"))
            )
            return login_button.is_displayed()
        except Exception:
            return False  # Return False if the element is not found or times out
