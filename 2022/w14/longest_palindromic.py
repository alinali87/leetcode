class Solution:
    def get_palindrome(self, left, right, s, init_len):
        begin = left
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                init_len += 2
                begin = left
                left -= 1
                right += 1
            else:
                break
        return init_len, begin

    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        begin = 0
        for middle in range(1, len(s)):
            cur_len, cur_begin = self.get_palindrome(middle - 1, middle, s, 0)
            if cur_len > max_len:
                max_len = cur_len
                begin = cur_begin
            cur_len, cur_begin = self.get_palindrome(middle - 1, middle + 1, s, 1)
            if cur_len > max_len:
                max_len = cur_len
                begin = cur_begin
        return s[begin:begin + max_len]


def test():
    solution = Solution()
    s = "babad"
    assert solution.longestPalindrome(s) == "bab"
    s = "cbbd"
    assert solution.longestPalindrome(s) == "bb"
    s = "aaaa"
    assert solution.longestPalindrome(s) == "aaaa"
    s = "abb"
    assert solution.longestPalindrome(s) == "bb"
