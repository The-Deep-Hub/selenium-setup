import logging
from abc import ABC, abstractmethod

from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.ie.options import Options as IEOptions
from selenium.webdriver.ie.webdriver import WebDriver as IEWebDriver
from webdriver_manager.microsoft import IEDriverManager

from selenium import webdriver
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from .webdriver_setup import WebDriverSetup, setup_logging

setup_logging()
logger = logging.getLogger(__name__)

class BaseDriverSetup(WebDriverSetup, ABC):
    """
    Abstract base class for WebDriver setups. Provides common functionality for
    handling options and creating WebDriver instances.
    """
    def __init__(self, additional_options: dict[str, str | None] | None = None, **kwargs):
        super().__init__(**kwargs)
        self.additional_options = additional_options if additional_options else {}

    def setup_options(self, options: BaseOptions) -> None:
        """
        Set up options based on additional configuration.
        This method can be overridden for browser-specific options.
        """
        super().setup_options(options)
        for key, value in self.additional_options.items():
            if value is not None:
                options.add_argument(f"{key}={value}")

    @abstractmethod
    def create_default_options(self) -> BaseOptions:
        """Create and return default options for the specific browser."""
        pass

    @abstractmethod
    def get_driver_service(self) -> None:
        """Return the WebDriver service for the specific browser."""
        pass

    @abstractmethod
    def create_webdriver_instance(self, service, options) -> RemoteWebDriver:
        """Create the WebDriver instance using the provided service and options."""
        pass

    def get_driver(self, custom_options: BaseOptions | None = None) -> RemoteWebDriver:
        """
        Create and return a WebDriver instance with customizable options.

        Args:
            custom_options (BaseOptions, optional): If provided, these options
            will override the default options set in the class.

        Returns:
            RemoteWebDriver: An instance of the WebDriver with the specified options.
        
        Raises:
            WebDriverException: If the WebDriver initialization fails.
        """
        options = self.create_default_options() if custom_options is None else custom_options
        try:
            service = self.get_driver_service()
            driver = self.create_webdriver_instance(service, options)
            logger.info(f"{type(driver).__name__} WebDriver setup complete.")
            return driver
        except WebDriverException as e:
            logger.error(f"Failed to initialize WebDriver: {e}")
            raise

""" CHROME DRIVER SETUP CLASS """

class ChromeDriverSetup(BaseDriverSetup):
    def create_default_options(self) -> ChromeOptions:
        """Create and return default ChromeOptions."""
        options = ChromeOptions()
        self.setup_options(options) 
        return options

    def get_driver_service(self) -> ChromeService:
        """Return the WebDriver service for Chrome."""
        return ChromeService(ChromeDriverManager().install())

    def create_webdriver_instance(self, service, options) -> ChromeWebDriver:
        """Create Chrome WebDriver instance."""
        return webdriver.Chrome(service=service, options=options)

""" FIREFOX DRIVER SETUP CLASS """

class FirefoxDriverSetup(BaseDriverSetup):
    def create_default_options(self) -> FirefoxOptions:
        """Create and return default FirefoxOptions."""
        options = FirefoxOptions()
        self.setup_options(options) 
        return options

    def get_driver_service(self) -> FirefoxService:
        """Return the WebDriver service for Firefox."""
        return FirefoxService(GeckoDriverManager().install())

    def create_webdriver_instance(self, service, options) -> FirefoxWebDriver:
        """Create Firefox WebDriver instance."""
        return webdriver.Firefox(service=service, options=options)
    
""" EDGE DRIVER SETUP CLASS """

class EdgeDriverSetup(BaseDriverSetup):
    def create_default_options(self) -> EdgeOptions:
        """Create and return default EdgeOptions."""
        options = EdgeOptions()
        self.setup_options(options) 
        return options

    def get_driver_service(self) -> EdgeService:
        """Return the WebDriver service for Edge."""
        return EdgeService(EdgeChromiumDriverManager().install())

    def create_webdriver_instance(self, service, options) -> EdgeWebDriver:
        """Create Edge WebDriver instance."""
        return webdriver.Edge(service=service, options=options)

""" INTERNET EXPLORER SETUP CLASS"""

class IEDriverSetup(BaseDriverSetup):
    def create_default_options(self) -> IEOptions:
        """Create and return default IEOptions."""
        options = IEOptions()
        self.setup_options(options)  
        return options

    def get_driver_service(self) -> IEService:
        """Return the WebDriver service for IE."""
        return IEService(IEDriverManager().install())

    def create_webdriver_instance(self, service, options) -> IEWebDriver:
        """Create IE WebDriver instance."""
        return webdriver.Ie(service=service, options=options)