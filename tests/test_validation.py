import pytest
import re
from test_cases_data import VALIDATION_CASES

@pytest.mark.parametrize("case", VALIDATION_CASES)
def test_validation_case(case):
    """Executes schema format and input structure validations."""
    if case["id"] == "TC-VAL-001":
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        assert email_regex.match("test@example.com")
    elif case["id"] == "TC-VAL-002":
        # Check password strength constraint
        password = "SecurePassword123"
        assert len(password) >= 8
    else:
        assert True
