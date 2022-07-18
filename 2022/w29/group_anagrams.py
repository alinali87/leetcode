from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def encode_anagram(s: str) -> str:
            """Return a string where the number on i-th position is the count of i-th letter in the original string"""
            counts = [0] * 26  # 26 letters in english alphabet
            for ch in s:
                idx = ord(ch) - 97
                counts[idx] += 1
            return ','.join(map(str, counts))

        ans = defaultdict(list)
        for s in strs:
            key = encode_anagram(s)
            ans[key].append(s)
        return list(ans.values())


sol = Solution()
strs = ["bdddddddddd","bbbbbbbbbbc"]
a = sol.groupAnagrams(strs)
print(a)
