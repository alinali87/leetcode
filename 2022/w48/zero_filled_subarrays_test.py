from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        nums.append(1)  # append any number != 0, to avoid situation when the last num == 0
        n, ans, c = len(nums), 0, 0
        if n == 0:
            return ans
        # iterate over nums
        # if zero and prev not exists --> c = 1
        # if zero and prev zero --> c += 1
        # if zero and prev not zero --> c = 1
        # if not zero --> ans += arithmetic progression sum
        for i, v in enumerate(nums):
            if i == 0 and v == 0:
                c = 1
            elif v == 0 and nums[i-1] == 0:
                c += 1
            elif v == 0 and nums[i-1] != 0:
                c = 1
            else:
                ans += (1 + c) * c // 2
                c = 0
        return ans


sol = Solution()
nums = [1,3,0,0,2,0,0,4]
a = sol.zeroFilledSubarray(nums)
assert a == 6, f'Test #1 {nums=} failed, {a=}'

nums = [0,0,0,2,0,0]
a = sol.zeroFilledSubarray(nums)
assert a == 9, f'Test #2 {nums=} failed, {a=}'

nums = [2,10,2019]
a = sol.zeroFilledSubarray(nums)
assert a == 0, f'Test #3 {nums=} failed, {a=}'

nums = [0,-9,6,-5,0,0,8,0,0,3,-3]
a = sol.zeroFilledSubarray(nums)
assert a == 7, f'Test #4 {nums=} failed, {a=}'
