import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def base_url():
    """Returns the base URL of the frontend web application."""
    return os.getenv("REACT_APP_FRONTEND_URL", "http://localhost:3000")

@pytest.fixture(scope="function")
def driver():
    """Initializes and returns a Selenium WebDriver instance with standard configurations."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless for CI/CD compatibility
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Check if ChromeDriver is available in environment
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
    except Exception as e:
        print(f"WebDriver initialization failed: {e}")
        # In case driver is not found, fallback to warning rather than hard crash
        yield None
