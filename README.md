# Selenium WebDriver Setup Library
This library provides a flexible and customizable setup for managing Selenium WebDriver instances. It supports multiple browsers (Chrome, Firefox, Edge, and Internet Explorer) and includes the ability to customize browser options, handle WebDriver errors, and retry failed operations.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Driver Setup](#driver-setup)
  - [Supported Browsers](#supported-browsers)
  - [Dynamic Driver Options](#dynamic-driver-options)
- [Logging](#logging)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)


## Features

- Supports Chrome, Firefox, Edge, and Internet Explorer browsers.
- Dynamic WebDriver options configuration, including headless mode, proxy, user agents, and more.
- Error handling with retries and recovery mechanisms for WebDriver failures.
- Centralized logging configuration with custom log levels.
- A factory pattern to dynamically select WebDriver based on the browser type.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Install the required dependencies:

pip install -r requirements.txt

Dependencies include:

- selenium
- webdriver-manager

3. Ensure the config/logging.ini file is properly configured for logging.

## Usage

### Driver Setup

The library provides a flexible interface for setting up and customizing Selenium WebDriver instances. It supports different browsers and custom options, such as proxy settings, headless mode, and window size.

Example: Basic Chrome WebDriver Setup

You can create and configure a WebDriver for Chrome:

```bash 
from selenium_drivers.driver_factory import get_driver

# Create a basic Chrome WebDriver with default options
driver = get_driver('chrome')

# Navigate to a website
driver.get('https://www.example.com')
```
### Supported Browsers

You can use the following browsers by specifying the browser type in the get_driver() function:

- Chrome: 'chrome'
- Firefox: 'firefox'
- Edge: 'edge'
- Internet Explorer: 'ie'

### Dynamic Driver Options

You can pass additional WebDriver options, such as enabling headless mode, setting proxy, or window size, through the ```get_driver``` function:

```bash
from selenium_drivers.driver_factory import get_driver

# Example: Setting custom options for Chrome WebDriver
driver = get_driver(
    'chrome',
    proxy="http://myproxy:8080",
    headless=True,
    window_size="1920,1080"
)
```
This enables the dynamic configuration of the WebDriver for each browser, giving you control over browser behaviors.

### Example: Firefox WebDriver with Custom Options

```bash
driver = get_driver(
    'firefox', 
    proxy="http://anotherproxy:8080", 
    headless=False,
    disable_extensions=True
)
```

### Available Configuration Options
The WebDriver can be customized with the following options:

- proxy: The proxy server to be used (e.g., "http://proxy:8080").
- headless: Whether to run the browser in headless mode (True or False).
- window_size: Set a custom window size (e.g., "1920x1080").
- user_agent: Custom user-agent string.
- disable_extensions: Disable browser extensions.
- incognito: Enable incognito mode.
- sandbox: Enable or disable the browser's sandbox mode.
- disable_dev_shm_usage: Disable shared memory usage in containers.
- ignore_certificate_errors: Ignore SSL certificate errors.
- disable_gpu: Disable GPU hardware acceleration.
- log_level: Set log level (default is 3).
- disable_notifications: Disable browser notifications.
- disable_popup_blocking: Disable popup blocking in the browser.
- verbose: Enable verbose logging for the browser.
- disable_infobars: Disable infobars in the browser.
- start_fullscreen (bool): Start the browser in fullscreen mode.
- disable_save_password_bubble (bool): Disable the save password prompt.
- safebrowsing_disable_download_protection (bool): Disable Safe Browsing download protection.
- disable_browser_side_navigation (bool): Disable browser side navigation.
- no_proxy_server: Disable the proxy server for the browser.

Check the WebDriverSetup class in selenium_drivers.webdriver_setup where this list of options is defined.

## Logging
The library includes centralized logging configured via logging.ini. By default, logs are written to a scraper.log file, but this can be customized via the config/logging.ini file.

The logging configuration can be easily customized:

1. Modify the config/logging.ini file to adjust logging levels, file outputs, or formats.
2. Use the setup_logging() function from webdriver_setup.py to configure logging in your project.

## Example: Custom Logging 

To change the logging configuration, edit config/logging.ini:

```bash
[loggers]
keys=root

[handlers]
keys=fileHandler

[formatters]
keys=formatter

[logger_root]
level=INFO
handlers=fileHandler

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=formatter
args=('scraper.log', 'a')

[formatter_formatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

## Project Structure

The project follows a modular structure, allowing flexibility in the extension of browser-specific functionality.

selenium_drivers/
│
├── __init__.py                      # Package initialization
├── base_driver_setup.py             # Abstract base class for WebDriver setups
├── driver_factory.py                # Factory for initializing WebDriver instances
├── webdriver_setup.py               # Core WebDriver setup class
│
└── config/
    └── logging.ini                  # Logging configuration

- base_driver_setup.py: Defines the abstract base class BaseDriverSetup, which is used to create WebDriver setups for different browsers.
- webdriver_setup.py: Contains the WebDriverSetup class for configuring WebDriver options and handling errors.
- driver_factory.py: The factory function get_driver() is used to dynamically select the WebDriver based on the browser type.

## Contributing 
If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. Check contributing.md for more details.

## License
This project is licensed under the Apache License, Version 2.0. See the LICENSE file for more details.

