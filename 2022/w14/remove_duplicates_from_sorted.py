from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(1, len(nums)):
            curr = nums[right]
            if curr > nums[left]:
                left += 1
            # if left != right:
                nums[left] = curr
        return left + 1


def test():
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = s.removeDuplicates(nums)
    print()
    print(k)
    print(nums)

    nums = [1,1,1,2]
    k = s.removeDuplicates(nums)
    print(k)
    print(nums)


test()
