"""Test cases for the greater function."""

import pytest
from utility.comparison import greater

@pytest.mark.parametrize(
    "num_1, num_2, expected",
    [
        (7, 5, 7),
        (100, 200, 200),
        (-5, -5, -5),
    ]
)
def test_greater(num_1, num_2, expected):
    result = greater(num_1, num_2)
    assert result == expected
