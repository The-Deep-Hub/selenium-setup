import os
import sys
import time
import logging
import logging.config

from typing import Callable, Any

from selenium.webdriver.common.options import BaseOptions
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException

def setup_logging(config_path:str='config/logging.ini', default_level:int=logging.INFO):
    """Setup logging configuration from a specified path.

    Arguments:
    config_path -- string, path to the logging configuration file (default 'config/logging.ini')
    default_level -- logging level, default to logging.INFO if configuration file is not found
    """
    if os.path.exists(config_path):
        logging.config.fileConfig(config_path, disable_existing_loggers=False)
        logging.info("Logging configured successfully using {}".format(config_path))
    else:
        logging.basicConfig(level=default_level)
        logging.warning("Failed to load configuration from {}. Using default logging settings.".format(config_path))

setup_logging()

class WebDriverSetup:
    def __init__(self, 
                 proxy: str | None = None, 
                 headless: bool = True, 
                 sandbox: bool = True, 
                 disable_dev_shm_usage: bool = False, 
                 ignore_certificate_errors: bool = False, 
                 disable_gpu: bool = False, 
                 log_level: int = 3, 
                 disable_notifications: bool = False, 
                 disable_popup_blocking: bool = False, 
                 user_agent: str | None = None, 
                 window_size: str | None = None, 
                 incognito: bool = False, 
                 disable_extensions: bool = False, 
                 verbose: bool = False, 
                 disable_infobars: bool = False, 
                 start_fullscreen: bool = False,
                 disable_save_password_bubble: bool = False, 
                 safebrowsing_disable_download_protection: bool = False,
                 disable_browser_side_navigation: bool = False, 
                 no_proxy_server: bool = False):
        """
        Initializes the WebDriver setup with various options.

        Args:
            proxy (str): Proxy server to be used.
            headless (bool): Enable headless mode (no browser UI).
            sandbox (bool): Enable or disable the browser's sandbox mode.
            disable_dev_shm_usage (bool): Disable shared memory usage in containers.
            ignore_certificate_errors (bool): Ignore SSL certificate errors.
            disable_gpu (bool): Disable GPU hardware acceleration.
            log_level (int): Set log level (default is 3).
            disable_notifications (bool): Disable browser notifications.
            disable_popup_blocking (bool): Disable popup blocking in the browser.
            user_agent (str): Custom user agent to use for the browser.
            window_size (str): Set custom window size for the browser (e.g., "1920x1080").
            incognito (bool): Enable incognito or private browsing mode.
            disable_extensions (bool): Disable browser extensions.
            verbose (bool): Enable verbose logging for the browser.
            disable_infobars (bool): Disable infobars in the browser.
            start_fullscreen (bool): Start the browser in fullscreen mode.
            disable_save_password_bubble (bool): Disable the save password prompt.
            safebrowsing_disable_download_protection (bool): Disable Safe Browsing download protection.
            disable_browser_side_navigation (bool): Disable browser side navigation.
            no_proxy_server (bool): Disable the proxy server for the browser.
        """
        self.proxy = proxy
        self.headless = headless
        self.sandbox = sandbox
        self.disable_dev_shm_usage = disable_dev_shm_usage
        self.ignore_certificate_errors = ignore_certificate_errors
        self.disable_gpu = disable_gpu
        self.log_level = log_level
        self.disable_notifications = disable_notifications
        self.disable_popup_blocking = disable_popup_blocking
        self.user_agent = user_agent
        self.window_size = window_size
        self.incognito = incognito
        self.disable_extensions = disable_extensions
        self.verbose = verbose
        self.disable_infobars = disable_infobars
        self.start_fullscreen = start_fullscreen
        self.disable_save_password_bubble = disable_save_password_bubble
        self.safebrowsing_disable_download_protection = safebrowsing_disable_download_protection
        self.disable_browser_side_navigation = disable_browser_side_navigation
        self.no_proxy_server = no_proxy_server

    def setup_options(self, options: BaseOptions) -> None:
        """
        Configure WebDriver options based on initialized settings.
        
        This method adds various options to the browser instance being used.

        Args:
            options (BaseOptions): Browser-specific options to configure.
        """
        if self.sandbox:
            options.add_argument("--no-sandbox")
        if self.disable_dev_shm_usage:
            options.add_argument("--disable-dev-shm-usage")
        if self.ignore_certificate_errors:
            options.add_argument("--ignore-certificate-errors")
        if self.disable_gpu:
            options.add_argument("--disable-gpu")
        if self.log_level is not None:
            options.add_argument(f"--log-level={self.log_level}")
        if self.disable_notifications:
            options.add_argument("--disable-notifications")
        if self.disable_popup_blocking:
            options.add_argument("--disable-popup-blocking")
        if self.proxy:
            options.add_argument(f"--proxy-server={self.proxy}")
        if self.headless:
            options.add_argument("--headless")
        if self.user_agent:
            options.add_argument(f"--user-agent={self.user_agent}")
        if self.window_size:
            options.add_argument(f"--window-size={self.window_size}")
        if self.incognito:
            options.add_argument("--incognito")
        if self.disable_extensions:
            options.add_argument("--disable-extensions")
        if self.verbose:
            options.add_argument("--verbose")
        if self.disable_infobars:
            options.add_argument("--disable-infobars")
        if self.start_fullscreen:
            options.add_argument("--start-fullscreen")
        if self.disable_save_password_bubble:
            options.add_argument("--disable-save-password-bubble")
        if self.safebrowsing_disable_download_protection:
            options.add_argument("--safebrowsing-disable-download-protection")
        if self.disable_browser_side_navigation:
            options.add_argument("--disable-browser-side-navigation")
        if self.no_proxy_server:
            options.add_argument("--no-proxy-server")
    
    def handle_webdriver_error(self, action: Callable[[], Any], error: Exception, retries: int = 3, delay:int = 2, action_desc:str = "operating the WebDriver") -> object:
        """
        Handles WebDriver errors and attempts to recover from them by retrying the failed action.
        
        Args:
            action (Callable): The action to retry.
            error (Exception): The caught error during WebDriver operation.
            retries (int): Number of retry attempts (default is 3).
            delay (int): Delay between retries (default is 2 seconds).
            action_desc (str): Description of the action being attempted.
        
        Returns:
            Any: The result of the retried action.
        
        Raises:
            Exception: If the retries fail, it raises the final exception.
        """

        logging.error(f"Error while {action_desc}: {error}")

        attempt = 0
        while attempt < retries:
            attempt += 1
            try:
                logging.info(f"Attempting {action_desc} - Try {attempt}/{retries}")
                return action()
            
            except (NoSuchElementException, TimeoutException) as e:
                logging.warning(f"Attempt {attempt} failed for {action_desc}: {e}")
                time.sleep(delay)

            except WebDriverException as e:
                logging.error(f"Critical WebDriver error during retry {attempt} for {action_desc}: {e}")
                if attempt >= retries:
                    logging.error("Maximum retry attempts reached, initiating recovery...")
                    self.attempt_recovery_or_exit()
                time.sleep(delay)

            except Exception as e:
                logging.critical(f"Unhandled error on attempt {attempt}: {e}")
                if attempt >= retries:
                    logging.error("Unhandled exception type after maximum retries, rethrowing...")
                    raise e  

    def attempt_recovery_or_exit(self) -> None:
        """
        Attempt to recover from a WebDriver failure by reinitializing the driver.

        If the recovery attempt fails, the function will log an error and exit.
        """
        try:
            logging.info("Attempting to recover the WebDriver...")
            self.get_driver()  

        except WebDriverException as e:
            logging.error("Recovery attempt failed, exiting: {0}".format(e))


