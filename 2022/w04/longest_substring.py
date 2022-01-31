from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if s == '' or k > len(s):
            return 0
        freq = Counter(s)
        for i, char in enumerate(s):
            if freq[char] < k:
                return max(self.longestSubstring(s[:i], k),  self.longestSubstring(s[i+1:], k))
        return len(s)

def test():
    s = Solution()
    assert s.longestSubstring("aaabb", 3) == 3
    assert s.longestSubstring("ababbc", 2) == 5
