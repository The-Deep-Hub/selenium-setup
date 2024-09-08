import unittest
from selenium_drivers.driver_factory import get_driver

class TestDriverFactory(unittest.TestCase):
    
    def test_get_chrome_driver(self):
        """Test getting Chrome WebDriver."""
        driver = get_driver('chrome')
        self.assertIsNotNone(driver)
        driver.quit()

    def test_get_firefox_driver(self):
        """Test getting Firefox WebDriver."""
        driver = get_driver('firefox')
        self.assertIsNotNone(driver)
        driver.quit()

    def test_invalid_browser(self):
        """Test invalid browser input."""
        with self.assertRaises(ValueError):
            get_driver('invalid_browser')
