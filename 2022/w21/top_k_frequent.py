from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        sorted_counts = sorted(((count, num) for num, count in counts.items()), reverse=True)[:k]
        return [num for count, num in sorted_counts]


def test():
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    a = s.topKFrequent(nums, k)
    assert sorted(a) == sorted([1, 2])
    nums = [1]
    k = 1
    a = s.topKFrequent(nums, k)
    assert a == [1]