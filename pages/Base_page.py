# base page class
# This is a class that contains all the common methods for all pages
# it is inherited by all page classes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def find(self, *locator):
        """Finds an element on the page."""
        return self.driver.find_element(*locator)
    
    def find_all(self, *locator):
        """Finds all elements on the page."""
        return self.driver.find_elements(*locator)
    
    def click(self, locator):
        """clicks on an element."""
        element = self.find(*locator).click()
        return element
    
    def send_key(self, locator, text):
        """sends keys to an element."""
        element = self.find(*locator)
        element.clear()
        return element.send_keys(text)
         
    def get_text(self, locator):
        """gets the text of an element."""
        element = self.find(*locator)
        return element.text
    
    def get_attrbute(self, locator, attribute):
        """gets the attribute of an element."""
        element = self.find(*locator)
        return element.get_attribute(attribute)
    
    def is_displayed(self, locator):
        """checks if an element is displayed."""
        element = self.find(*locator)
        return element.is_displayed()
    
    def is_enabled(self, locator):
        """checks if an element is enabled."""
        element = self.find(*locator)
        return element.is_enabled()
    
    def is_selected(self, locator):
        """checks if an element is selected."""
        element = self.find(*locator)
        return element.is_selected()
    
    def wait_for_element(self, locator, timeout=10):
        """waits for an element to be present."""
        wait = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return wait
    
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """waits for an element to be clickable."""
        wait = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        return wait
    
    def fluent_wait(self, locator, timeout=10, poll_frequency = 1):
        """waits for an element to be present."""
        wait = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
        return wait
    
    def get_title(self):
        """gets the title of the page."""
        return self.driver.title
        
    