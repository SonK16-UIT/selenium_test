import pytest
from selenium.webdriver.common.by import By
from tests.pages.login_page import LoginPage
from tests.pages.home_page import HomePage
from tests.utils.selenium_utils import wait_for_element

class TestLoginPage:
    def test_valid_login(self, driver):
        """
        Test valid login functionality by entering correct credentials and verifying navigation to the dashboard.
        """
        login_page = LoginPage(driver)
        login_page.open_page()

        wait_for_element(driver, By.ID, "email", timeout=10)
        login_page.enter_username("admin89@gmail.com")
        wait_for_element(driver, By.ID, "password", timeout=5)
        login_page.enter_password("ABCabc123!")
        login_page.click_login()

        assert login_page.verify_successful_login(), "Login failed, dashboard not displayed."

    @pytest.mark.parametrize("username, password, error_message", [
        ("invalid_user@example.com", "wrongPassword123", "Tài khoản không hợp lệ!"),
        ("admin89@gmail.com", "wrongPassword123", "Sai mật khẩu!"),
        ("", "ABCabc123!", "Email không hợp lệ!"),
        ("admin89@gmail.com", "", "Thiếu mật khẩu!"),
    ])
    def test_invalid_login(self, driver, username, password, error_message):
        """
        Test invalid login functionality with various username and password combinations.
        """
        login_page = LoginPage(driver)
        login_page.open_page()

        wait_for_element(driver, By.ID, "email", timeout=10)
        login_page.enter_username(username)
        wait_for_element(driver, By.ID, "password", timeout=5)
        login_page.enter_password(password)
        login_page.click_login()

        error_element = wait_for_element(driver, By.ID, "error_message", timeout=5)
        assert error_element.text == error_message, \
            f"Expected error message '{error_message}', but got '{error_element.text}'."

    def test_google_login_button_present(self, driver):
        """
        Test that the Google Login button is present and visible.
        """
        login_page = LoginPage(driver)
        login_page.open_page()

        google_button = wait_for_element(driver, By.XPATH, "//button[contains(text(), 'Đăng nhập với Google')]", timeout=5)
        assert google_button.is_displayed(), "Google login button is not displayed."

    def test_empty_form_submission(self, driver):
        """
        Test submitting the login form with empty fields.
        """
        login_page = LoginPage(driver)
        login_page.open_page()

        login_page.click_login()

        error_element = wait_for_element(driver, By.ID, "error_message", timeout=5)
        assert "Email không hợp lệ!" in error_element.text, "Error for empty form submission not displayed."

    def test_password_masking(self, driver):
        """
        Test that the password field masks the input.
        """
        login_page = LoginPage(driver)
        login_page.open_page()

        password_field = wait_for_element(driver, By.ID, "password", timeout=5)
        login_page.enter_password("password123")

        assert password_field.get_attribute("type") == "password", "Password is not masked."

    def test_homepage_navigate_login(self, driver):
        """
        Test valid login redirects to the homepage and allows for successful logout.
        """
        login_page = LoginPage(driver)
        home_page = HomePage(driver)

        login_page.open_page()

        wait_for_element(driver, By.ID, "email", timeout=10)
        login_page.enter_username("admin89@gmail.com")
        wait_for_element(driver, By.ID, "password", timeout=5)
        login_page.enter_password("ABCabc123!")
        login_page.click_login()

        # Verify successful login
        assert login_page.verify_successful_login(), "Login failed, dashboard not displayed."

        # Perform Logout
        home_page.click_logout()

        # Verify successful logout
        assert home_page.verify_successful_logout(), "Logout failed, still on homepage."

