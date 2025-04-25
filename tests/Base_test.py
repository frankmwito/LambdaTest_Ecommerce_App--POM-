# Base test class for the application
# This class contains the setup and teardown methods for the test cases.
# It also contains the common methods for all test cases.
# it is inherited by all test classes.

import pytest


@pytest.mark.usefixtures("driver_setup")
class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, driver_setup):
        """Setup method to be run before each test case."""
        print("Setup: Opening the browser and navigating to the URL.")
        self.driver = driver_setup
        
        yield self.driver # This will be the driver instance for the test 
        
        print("Teardown: Closing the browser.")
        
        
        