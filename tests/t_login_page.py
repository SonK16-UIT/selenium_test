import pytest
from tests.pages.login_page import LoginPage, wait_for_element  # Relative import
from selenium.webdriver.common.by import By


class TestLoginPage:
    def test_valid_login(self, driver):
        """
        Test valid login functionality by entering correct credentials and verifying navigation to the dashboard.
        """
        url = "https://home-automation-raspi.web.app/login"

        # Initialize the LoginPage with the driver from the fixture
        login_page = LoginPage(driver)

        # Open the login page
        login_page.open_page(url)

        # Wait for the page to load and the login form to appear
        wait_for_element(driver, By.ID, "email", timeout=10)

        # Enter Username and Password
        login_page.enter_username("admin89@gmail.com")
        wait_for_element(driver, By.ID, "password", timeout=5)  # Wait for password field
        login_page.enter_password("ABCabc123!")

        # Click the login button
        login_page.click_login()

        # Verify successful login
        assert login_page.verify_successful_login(), "Login failed, dashboard not displayed."

    @pytest.mark.parametrize("username, password, error_message", [
        ("invalid_user@example.com", "wrongPassword123", "Tài khoản không hợp lệ!"),
        ("admin89@gmail.com", "wrongPassword123", "Sai mật khẩu!"),
        ("", "ABCabc123!", "Email không hợp lệ!"),
        ("admin89@gmail.com", "", "Thiếu mật khẩu!")
    ])
    def test_invalid_login(self, driver, username, password, error_message):
        """
        Test invalid login functionality with various username and password combinations.
        """
        url = "https://home-automation-raspi.web.app/login"

        # Initialize the LoginPage with the driver from the fixture
        login_page = LoginPage(driver)

        # Open the login page
        login_page.open_page(url)

        # Wait for the login page to fully load
        wait_for_element(driver, By.ID, "email", timeout=10)

        # Enter Username and Password
        login_page.enter_username(username)
        wait_for_element(driver, By.ID, "password", timeout=5)
        login_page.enter_password(password)

        # Click the login button
        login_page.click_login()

        # Wait for potential error message using a more stable locator (XPath)
        # Locate the error message using a more stable locator (XPath)
        error_element = wait_for_element(driver, By.ID, "error_message", timeout=5)

        # Assert that the error message matches the expected message
        assert error_element.text == error_message, f"Expected error message '{error_message}', but got '{error_element.text}'."
