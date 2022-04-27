from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1, 2, 3, 4, 5 -> 4, 5, 1, 2, 3
        k = k % len(nums)
        if k == 0:
            return

        def reverse(lst, left, right) -> None:
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)


def test():
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    s.rotate(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]
