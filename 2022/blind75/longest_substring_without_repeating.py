class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ans = 1
        left = 0
        seen = {s[0]: 0}
        for right in range(1, len(s)):
            if s[right] in seen:
                left = max(seen[s[right]] + 1, left)
                seen[s[right]] = right
            ans = max(ans, right - left + 1)
            seen[s[right]] = right
        return ans


def test():
    sol = Solution()
    s = "abcabcbb"
    assert sol.lengthOfLongestSubstring(s) == 3
    s = "bbbbb"
    assert sol.lengthOfLongestSubstring(s) == 1
    s = "pwwkew"
    assert sol.lengthOfLongestSubstring(s) == 3
    s = "abba"
    assert sol.lengthOfLongestSubstring(s) == 2

