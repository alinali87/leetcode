from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        f = strs[0]
        for i, char in enumerate(f):
            for s in strs:
                if i >= len(s) or s[i] != char:
                    return f[:i]
        return f


def test(mine, expected):
    assert mine == expected, f'mine: {mine}, expected: {expected}'


sol = Solution()
strs = ["flower","flow","flight"]
test(sol.longestCommonPrefix(strs), "fl")
strs = ["dog","racecar","car"]
test(sol.longestCommonPrefix(strs), "")

