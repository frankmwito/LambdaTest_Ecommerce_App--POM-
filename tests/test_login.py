# test methods for login page
# This is where assertions are performed to verify the functionality of the login page.

from utilities.test_data import TestData
from pages.Login_page import LoginPage
import pytest
from tests.Base_test import BaseTest

class TestLogin(BaseTest):
    """Test class for the Login page."""
    
    def test_valid_credentials(self):
        """Test case for valid login credentials."""
        login_page = LoginPage(self.driver)
        login_page.set_email_address(TestData.email)
        login_page.set_passwword(TestData.password)
        login_page.click_login_button()
        title = "My Account"
        actual_title = login_page.get_title()
        assert actual_title == "My Account", f"Expected title: {title}"
    
    def test_invalid_credentials(self):
        """Test case for invalid Login credentials."""
        login_page = LoginPage(self.driver)
        login_page.log_into_application(
            "Invalid_email", "Invalid_password")
        actual_message = login_page.get_warning_message()
        assert actual_message.__contains__("Warning")
        