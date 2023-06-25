import pytest
from maximum_product_subarray import Solution
from cases import CASES


IDS = [case.name for case in CASES]
ARGS = [case.test.args for case in CASES]
EXPECTED = [case.test.expected for case in CASES]


@pytest.mark.parametrize('args, expected', zip(ARGS, EXPECTED), ids=IDS)
def test_solution(args, expected):
    sol = Solution()
    assert expected == sol.maxProduct(args)
