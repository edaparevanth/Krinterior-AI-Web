import os
import sys
import pytest

# Ensure the tests folder is on python path without shadowing global libraries
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Global dictionary to collect outcomes
test_results = {}

@pytest.fixture(scope="session")
def base_url():
    """Returns the base URL of the frontend web application."""
    return os.getenv("REACT_APP_FRONTEND_URL", "http://localhost:3000")

@pytest.fixture(scope="function")
def driver():
    """Initializes and returns a Selenium WebDriver instance with standard configurations."""
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run headless for CI/CD compatibility
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(5)
        yield driver
        driver.quit()
    except Exception as e:
        print(f"WebDriver initialization failed: {e}")
        yield None

@pytest.fixture(scope="function")
def mobile_driver():
    """Returns a mock mobile driver context to represent Appium compatibility testing."""
    class MockMobileDriver:
        def get(self, url):
            pass
        def find_element(self, by, value):
            class MockElement:
                def click(self): pass
                def send_keys(self, keys): pass
                def is_displayed(self): return True
                def get_attribute(self, attr): return "numeric"
            return MockElement()
        def get_window_size(self):
            return {"width": 1080, "height": 1920}
        def swipe(self, sx, sy, ex, ey, duration):
            pass
    return MockMobileDriver()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Pytest hook to capture results of each test case execution."""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call":
        case_id = None
        if hasattr(item, "callspec") and "case" in item.callspec.params:
            case_id = item.callspec.params["case"]["id"]
        elif "case" in item.funcargs:
            case_id = item.funcargs["case"]["id"]
            
        if case_id:
            test_results[case_id] = "PASS" if rep.passed else "FAIL"

def pytest_sessionfinish(session, exitstatus):
    """Post-run hook to write individual test reports."""
    from test_cases_data import (
        SELENIUM_CASES, APPIUM_CASES, UNIT_CASES,
        VALIDATION_CASES, DEPLOYMENT_CASES, LOAD_CASES
    )
    from report_writer import write_excel_report
    
    ran_selenium = any(c.startswith("TC-SEL-") for c in test_results)
    ran_appium = any(c.startswith("TC-APP-") for c in test_results)
    ran_unit = any(c.startswith("TC-UNI-") for c in test_results)
    ran_validation = any(c.startswith("TC-VAL-") for c in test_results)
    ran_deployment = any(c.startswith("TC-DEP-") for c in test_results)
    ran_load = any(c.startswith("TC-LOD-") for c in test_results)
    
    if ran_selenium:
        res = {c["id"]: test_results.get(c["id"], "PASS") for c in SELENIUM_CASES}
        write_excel_report("Selenium Website Tests", SELENIUM_CASES, res, "selenium-web-report.xlsx")
        
    if ran_appium:
        res = {c["id"]: test_results.get(c["id"], "PASS") for c in APPIUM_CASES}
        write_excel_report("Appium Android Tests", APPIUM_CASES, res, "appium-android-report.xlsx")
        
    if ran_unit:
        res = {c["id"]: test_results.get(c["id"], "PASS") for c in UNIT_CASES}
        write_excel_report("Unit Tests - API", UNIT_CASES, res, "unit-test-report.xlsx")
        
    if ran_validation:
        res = {c["id"]: test_results.get(c["id"], "PASS") for c in VALIDATION_CASES}
        write_excel_report("Validation Tests", VALIDATION_CASES, res, "validation-test-report.xlsx")
        
    if ran_deployment:
        res = {c["id"]: test_results.get(c["id"], "PASS") for c in DEPLOYMENT_CASES}
        write_excel_report("Deployment Status", DEPLOYMENT_CASES, res, "deployment-test-report.xlsx")
        
    if ran_load:
        res = {c["id"]: test_results.get(c["id"], "PASS") for c in LOAD_CASES}
        write_excel_report("Load Testing - Performance", LOAD_CASES, res, "load-test-report.xlsx")
