# Change password page
# This page contains the locators and methods for the change password page of the application.
# It inherits from the BasePage class.


from pages.Base_page import BasePage
from pages.my_account_page import MyAccountPage
from selenium.webdriver.common.by import By

class ChangePasswordPage(BasePage):
    """Store all locators for the Change password page."""
    password_field = (By.ID, "input-password")
    confirm_password = (By.ID, "imput-confirm")
    continue_button = (By.XPATH, "//input[@value='Continue']")
    confirmation_error_message = (By.XPATH, "//div[@class='text-danger']")
    
    def __init__(self, driver):
        super().__init__(driver)
        
        
    def change_password(self, password, confirm_password):
        """Change the password."""
        self.send_key(self.password_field, password)
        self.send_key(self.confirm_password, confirm_password)
        self.click(self.continue_button)
        return MyAccountPage(self.driver)
    
    def get_confirmation_error_message(self):
        """Get the confirmation error message."""
        return self.get_text(self.confirmation_error_message)