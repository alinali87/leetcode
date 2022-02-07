# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            sym = s[right]
            if sym in prev:
                left = max(left, prev[sym] + 1)
            max_length = max(max_length, right - left + 1)
            prev[sym] = right
        return max_length


def test():
    sol = Solution()
    s = "abcabcbb"
    assert sol.lengthOfLongestSubstring(s) == 3
    s = "bbbbb"
    assert sol.lengthOfLongestSubstring(s) == 1
    s = "pwwkew"
    assert sol.lengthOfLongestSubstring(s) == 3
    s = "tmmzuxt"
    assert sol.lengthOfLongestSubstring(s) == 5

test()
