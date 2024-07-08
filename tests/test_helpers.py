"""@author: jldupont"""
import pytest
from pygcloud.helpers import validate_name


@pytest.mark.parametrize("input,expected", [
    ("name777", True),
    ("9cannot_start_with_digit", False),
    ("name__666", True),
    ("name--invalid_double-dash", False)
])
def test_validate_name(input, expected):
    assert validate_name(input) == expected
