from .base_driver_setup import ChromeDriverSetup, FirefoxDriverSetup, EdgeDriverSetup, IEDriverSetup

def get_driver(browser: str, **kwargs):
    """
    Factory method to instantiate a web driver based on the browser type and custom options.
    
    Args:
        browser (str): The type of browser ('chrome', 'firefox', 'edge', 'ie').
        **kwargs: Additional options to pass to the driver setup (e.g., proxy, headless).

    Returns:
        WebDriver: An instance of a WebDriver for the specified browser.
    
    Raises:
        ValueError: If the browser type is unsupported.
    """
    if browser.lower() == 'chrome':
        return ChromeDriverSetup(**kwargs).get_driver()
    
    elif browser.lower() == 'firefox':
        return FirefoxDriverSetup(**kwargs).get_driver()
    
    elif browser.lower() == 'edge':
        return EdgeDriverSetup(**kwargs).get_driver()
    
    elif browser.lower() == 'ie':
        return IEDriverSetup(**kwargs).get_driver()
    
    else:
        raise ValueError(f"Unsupported browser type: {browser}")
    