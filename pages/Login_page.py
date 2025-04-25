# Login page for the application
# This page contains the locators and methods for the login page of the application.
# It inherits from the BasePage class.


from pages.Base_page import BasePage
from pages.my_account_page import MyAccountPage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    """Store all Locators for the Login page."""
    email_address_field = (By.ID, "input-email")
    password_field = (By.ID, "input-password")
    login_button = (By.XPATH, "//input[@value='Login']")
    warning_message = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def set_email_address(self, email_address): #argument containing the value to be set in the email field
        """Set the email address in the email field."""
        self.send_key(self.email_address_field, email_address)
        
    def set_passwword(self, password):
        """Set the password in the password field."""
        self.send_key(self.password_field, password)
        
    def click_login_button(self):
        """Click the Login button."""
        self.click(self.login_button)
        return MyAccountPage(self.driver)
    
    def log_into_application(self, email, password):
        self.set_email_address(email)
        self.set_passwword(password)
        self.click_login_button()
    
    def get_warning_message(self):
        return self.get_text(self.warning_message)