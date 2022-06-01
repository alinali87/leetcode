from typing import List


class Solution:
    def get(self, i, nums: List[int]) -> int:
        t = (i + self.k) % self.n
        return nums[t]

    def search(self, nums: List[int], target: int) -> int:
        self.k = 0
        self.n = len(nums)
        l = 0
        r = len(nums) - 1

        if nums[l] > nums[r]:
            while r - l > 1:
                mid = (l + r) // 2
                if nums[mid] > nums[r]:
                    l = mid
                else:
                    r = mid
            self.k = r

        l = 0
        r = self.n - 1
        if (target < self.get(l, nums)) or (target > self.get(r, nums)):
            return -1
        if (target == self.get(l, nums)):
            return ((l + self.k) % self.n)
        if (target == self.get(r, nums)):
            return ((r + self.k) % self.n)
        while (r - l > 1):
            t = (r + l) // 2
            val = self.get(t, nums)
            if (val == target):
                return ((t + self.k) % self.n)
            if (target > val):
                l = t
            else:
                r = t
        return -1


def test():
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    a = s.search(nums, target)
    assert a == 4

