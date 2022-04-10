from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            curr = min(height[left], height[right]) * (right - left)
            area = max(area, curr)
        return area


def test():
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    a = s.maxArea(height)
    assert a == 49
    height = [1, 1]
    a = s.maxArea(height)
    assert a == 1
