from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count_pos = [0] * (10 ** 4)
        count_neg = [0] * (10 ** 4)
        largest = -float('inf')
        for num in nums:
            if num < 0:
                count_neg[num] += 1
            else:
                count_pos[num] += 1
            largest = max(largest, num)
        cumcount = 0
        for i in range(largest, -1, -1):
            cumcount += count_pos[i]
            if cumcount >= k:
                return i
        for i in range(10 ** 4 - 1, -1, -1):
            cumcount += count_neg[i]
            if cumcount >= k:
                return i - len(count_neg)


def test():
    s = Solution()
    nums = [-1,-1]
    a = s.findKthLargest(nums, 2)
    assert a == -1