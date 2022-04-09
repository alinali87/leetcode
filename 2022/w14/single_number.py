from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        ans = 0
        for num in nums:
            if num in seen:
                ans -= num
            else:
                seen.add(num)
                ans += num
        return ans



def test():
    s = Solution()
    nums = [2, 2, 1]
    a = s.singleNumber(nums)
    assert a == 1
    nums = [4,1,2,1,2]
    a = s.singleNumber(nums)
    assert a == 4
    nums = [1]
    a = s.singleNumber(nums)
    assert a == 1

