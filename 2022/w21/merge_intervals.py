from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_int = sorted(intervals)
        curr = sorted_int[0]
        ans = []
        for interval in sorted_int:
            if curr[1] >= interval[0]:
                curr[1] = max(curr[1], interval[1])
            else:
                ans.append(curr)
                curr = interval
        ans.append(curr)
        return ans


def test():
    s = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    a = s.merge(intervals)
    assert a == [[1,6],[8,10],[15,18]]

