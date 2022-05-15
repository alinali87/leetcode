# It's hard to invent the recursive solution of-the-cuff
from typing import List


class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
             we will sort your return value in output
    """
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path):
            ans.append(path)
            for i, n in enumerate(nums):
                if i > 0 and n == nums[i - 1]:
                    continue
                dfs(nums[i + 1:], path + [n])

        ans = []
        nums.sort()
        dfs(nums, [])
        return ans


def test():
    # example 1
    s = Solution()
    nums = [0]
    a = s.subsets_with_dup(nums)
    assert sorted(a) == [[], [0]]
    # example 2
    nums = [1, 2, 2]
    a = s.subsets_with_dup(nums)
    assert sorted(a) == sorted([[2], [1], [1, 2, 2], [2, 2], [1, 2], []])
