# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev = {}
        max_count = 0
        count = 0
        i = 0
        while i < len(s):
            sym = s[i]
            if sym in prev:
                i = prev[sym]
                prev = {}
                count = 0
            else:
                prev[sym] = i
                count += 1
            max_count = max(max_count, count)
            i += 1
        return max_count

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
