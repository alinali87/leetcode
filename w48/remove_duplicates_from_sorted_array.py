from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k = 1
        while i < len(nums) and k < len(nums):
            if nums[i] == nums[k]:
                k += 1
                while k < len(nums):
                    if nums[i] != nums[k]:
                        nums[i + 1] = nums[k]
                        i += 1
                        break
                    else:
                        k += 1
            else:
                i += 1
                k = max(k, i + 1)
        return i + 1

lst = [1, 2, 2, 3, 4, 5, 5, 5]
k = Solution().removeDuplicates(lst)
print("k:", k)
print(lst)