class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        ans = 0
        left = 0
        for right, char in enumerate(s):
            if char in seen and left <= seen[char]:
                left = seen[char] + 1
            else:
                ans = max(ans, right - left + 1)
            seen[char] = right
        return ans
