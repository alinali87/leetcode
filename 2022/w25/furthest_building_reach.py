from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        a = []
        for i in range(1, len(heights)):
            delta = heights[i] - heights[i - 1]
            if delta > 0:
                heapq.heappush(a, delta)
                if len(a) > ladders:
                    bricks -= heapq.heappop(a)
                if bricks < 0:
                    return i - 1
        return len(heights) - 1


def test(a, b):
    assert a == b, f'a: {a}, b: {b}'


sol = Solution()
heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
test(sol.furthestBuilding(heights, bricks, ladders), 4)
