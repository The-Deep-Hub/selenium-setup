import unittest
from selenium.common.exceptions import WebDriverException
from selenium_drivers.base_driver_setup import ChromeDriverSetup
from unittest.mock import patch


class TestChromeDriverSetup(unittest.TestCase):
    
    def setUp(self):
        self.chrome_setup = ChromeDriverSetup()

    def test_driver_initialization(self):
        """Test if the Chrome WebDriver initializes successfully."""
        driver = self.chrome_setup.get_driver()
        self.assertIsNotNone(driver)
        driver.quit() 

    def test_custom_options(self):
        """Test Chrome WebDriver with custom options."""
        chrome_setup = ChromeDriverSetup(additional_options={'--headless': None})
        driver = chrome_setup.get_driver()
        self.assertTrue(driver.capabilities['goog:chromeOptions']['args'], '--headless')
        driver.quit()

    def test_invalid_driver(self):
        """Test Chrome WebDriver initialization failure."""
        with self.assertRaises(WebDriverException):
            chrome_setup = ChromeDriverSetup(additional_options={'--invalid-arg': None})
            chrome_setup.get_driver()
    
    @patch('selenium.webdriver.Chrome')
    def test_invalid_driver(self, MockChrome):
        """Test Chrome WebDriver initialization failure."""
        # Set the mock to raise WebDriverException when called
        MockChrome.side_effect = WebDriverException("Mocked WebDriver failure")
        
        chrome_setup = ChromeDriverSetup()

        # Now assert that the WebDriverException is raised
        with self.assertRaises(WebDriverException):
            chrome_setup.get_driver()