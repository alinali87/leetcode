from typing import (
    List,
)

class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def max_sub_array_len(self, nums: List[int], k: int) -> int:
        max_len = 0
        d = {0: -1}  # key - cumsum, value - first occurrence index
        cumsum = 0
        for i, num in enumerate(nums):
            cumsum += num
            if cumsum - k in d:
                max_len = max(max_len, i - d[cumsum - k])
            d[cumsum] = d.get(cumsum, i)
        return max_len


def test():
    s = Solution()
    nums = [1, -1, 5, -2, 3]
    k = 3
    a = s.max_sub_array_len(nums, k)
    assert a == 4


test()