import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="session")
def appium_server_url():
    """Returns the address of the running Appium server."""
    return "http://localhost:4723"

@pytest.fixture(scope="function")
def mobile_driver(appium_server_url):
    """Initializes and returns an Appium WebDriver for Android Testing."""
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android Emulator"
    
    # Can configure to test via native APK or Chrome mobile browser
    options.browser_name = "Chrome"  
    options.set_capability("newCommandTimeout", 300)
    options.set_capability("chromedriverExecutableDir", "./drivers")
    
    try:
        driver = webdriver.Remote(appium_server_url, options=options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
    except Exception as e:
        print(f"Appium Server/Driver initialization failed: {e}")
        # Return None so test suites can skip gracefully on systems without Appium running
        yield None
