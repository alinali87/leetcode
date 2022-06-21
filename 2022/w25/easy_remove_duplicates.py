from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # sr - slow runner, fr - fast runner moves ahead slow runner
        sr = 0
        fr = 1
        # if fr is gte len(nums) we have traversed all the numbers
        while fr < len(nums):
            # sr stands on the last non-duplicated number, fr is somewhere ahead
            # if two numbers is equal sr can not proceed so fr moves forward
            if nums[sr] == nums[fr]:
                fr += 1
            else:
                # if two numbers are different we have found a new non-duplicate number
                # let's move sr one step and put this new number on sr place
                # if sr and fr were close to each other, then we just take a num a put it on the same place
                # if fr was several steps ahead sr, then we put the fr number on the place next to sr was
                # and sr continues to show the last non-duplicate number
                sr += 1
                nums[sr] = nums[fr]
                fr += 1
        return sr + 1


def test(a, b):
    assert a == b, f'a: {a}, b: {b}'


sol = Solution()
nums = [1,1,2]
test(sol.removeDuplicates(nums), 2)

nums = [0,0,1,1,1,2,2,3,3,4]
test(sol.removeDuplicates(nums), 5)
