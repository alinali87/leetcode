# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for w in strs:
            key = tuple(sorted(list(w)))
            d[key].append(w)
        return d.values()


def test():
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]] == sorted(map(sorted, s.groupAnagrams(strs)), key=lambda x: len(x))

