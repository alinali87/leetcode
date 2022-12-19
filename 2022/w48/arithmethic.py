from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n-2):
            diff = nums[i+1] - nums[i]
            for j in range(i + 1, n):
                if nums[j] - nums[j-1] == diff:
                    if j - i + 1 >= 3:
                        # print(f'{diff=}')
                        # print(f'{i=}, {j=}, {nums[i:j + 1]}')
                        ans += 1
                else:
                    break

        return ans


sol = Solution()
# nums = [1,2,3,8,9,10]
nums = [1,2,3,4]
a = sol.numberOfArithmeticSlices(nums)
print(a)