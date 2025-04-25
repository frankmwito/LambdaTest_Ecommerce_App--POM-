# Cross Browser Webdriver Setup
# Webdriver setup for crossbrowser testing

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.test_data import TestData

@pytest.fixture(params=["chrome", "firefox", "edge"], scope= "module")
def driver_setup(request):
    if request.param == "chrome":
        service = ChromeService()
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    elif request.param == "firefox":
        service = FirefoxService()
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    elif request.param == "edge":
        service = EdgeService()
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {request.param}")
    
    driver.get(TestData.url)
    driver.maximize_window()
    yield driver
    
    driver.close()