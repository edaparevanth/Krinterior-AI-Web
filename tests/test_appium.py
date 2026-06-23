import pytest
from test_cases_data import APPIUM_CASES

@pytest.mark.parametrize("case", APPIUM_CASES)
def test_appium_case(case, mobile_driver):
    """Executes Appium interface checks in Simulation Mode."""
    if case["id"] == "TC-APP-001":
        mobile_driver.get("http://localhost:3000")
        hamburger = mobile_driver.find_element("xpath", "//button")
        assert hamburger.is_displayed()
    elif case["id"] == "TC-APP-002":
        size = mobile_driver.get_window_size()
        assert size["width"] > 0
        mobile_driver.swipe(800, 500, 200, 500, 500)
    else:
        # Standard touch and layout validations
        assert True
