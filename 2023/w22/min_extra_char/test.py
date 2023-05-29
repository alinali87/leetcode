import pytest
from min_extra_char import Solution
from cases import CASES


IDS = [case.name for case in CASES]
EXPECTED = [case.test.expected for case in CASES]
DATA = [case.test.data for case in CASES]

sol = Solution()


@pytest.mark.parametrize('data, expected', zip(DATA, EXPECTED), ids=IDS)
def test_min_extra_char(data, expected):
    assert sol.minExtraChar(*data) == expected
