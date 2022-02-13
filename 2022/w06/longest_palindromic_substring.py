# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass


def test():
    sol = Solution()
    s = "babad"
    assert sol.longestPalindrome(s) == "bab"
    s = "cbbd"
    assert sol.longestPalindrome(s) == "bb"

