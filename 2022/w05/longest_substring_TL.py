from collections import defaultdict


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # corner case
        if len(s) == 1 and k == 1:
            return 1
        result = 0
        for left in range(len(s)):
            d = defaultdict(int)
            d[s[left]] = 1
            for right in range(left + 1, len(s)):
                # ~~left is position while right is the border~~
                # And now left is the position and right is the position also.
                d[s[right]] += 1
                freq = min(d.values())
                if freq >= k:
                    result = max(result, right - left + 1)
        return result




def test():
    s = Solution()
    assert s.longestSubstring("aaabb", 3) == 3
    assert s.longestSubstring("ababbc", 2) == 5
    assert s.longestSubstring("aaabbb", 3) == 6         
    # TL on test 33 of 35