# Change password tests
import pytest
from tests.Base_test import BaseTest
from pages.Changepassword_page import ChangePasswordPage
from pages.Login_page import LoginPage
from utilities.test_data import TestData
from pages.Base_page import BasePage
from pages.my_account_page import MyAccountPage

class TestChangePassword(BaseTest):
    """Test class for the change password page."""
    def test_change_password(self):
        """Test the change password functionality. """
        login_page = LoginPage(self.driver)
        change_password_page = ChangePasswordPage(self.driver)
        my_account_page = MyAccountPage(self.driver)
        expected_message = "Password confirmation does not match password!"
        login_page.log_into_application(
            TestData.email, TestData.password
        )
        wait1 = BasePage(self.driver)
        # Wait for the Change Password button (or link) to be clickable
        wait1.wait_for_element_to_be_clickable(
            ChangePasswordPage.password, 10
        )

        # Now click on Change Password
        my_account_page.click(ChangePasswordPage.password)
        change_password_page.change_password("InvalidPassword", "InvalidConfirmPassword")
        actual_message = change_password_page.get_confirmation_error_message()
        assert actual_message == expected_message, f"Expected message: {expected_message}"
        
        