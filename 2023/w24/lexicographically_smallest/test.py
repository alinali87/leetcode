import pytest
from lexicographically_smallest import Solution
from cases import CASES


IDS = [case.name for case in CASES]
EXPECTED = [case.test.expected for case in CASES]
ARGS = [case.test.args for case in CASES]

sol = Solution()


@pytest.mark.parametrize('args, expected', zip(ARGS, EXPECTED), ids=IDS)
def test_solution(args, expected):
    assert expected == sol.smallestString(*args)
