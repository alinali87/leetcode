class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        max_len = 1
        begin = 0

        # for length==1 it's palidromic for any substring
        for i in range(len(s)):
            dp[i][i] = 1

        # for length==2
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                if 2 > max_len:
                    max_len = 2
                    begin = i

        # for any other length
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = 1
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        begin = i

        return s[begin:begin + max_len]


def test():
    solution = Solution()
    # s = "babad"
    # assert solution.longestPalindrome(s) == "bab"
    # s = "cbbd"
    # assert solution.longestPalindrome(s) == "bb"
    s = "aaaaa"
    a = solution.longestPalindrome(s) == "aaaaa"
    print(a)
    # assert solution.longestPalindrome(s) == "aaaaa"
    # s = "abb"
    # assert solution.longestPalindrome(s) == "bb"