class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        seq = [x if x == '0' else '' for x in s]
        res = len(''.join(seq))
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                continue
            seq[i] = '1'
            if int(''.join(seq), 2) > k:
                return res
            res += 1
        return res



def test(a, b):
    assert a == b, f'a: {a}, b: {b}'


sol = Solution()
s = "1001010"
k = 5
test(sol.longestSubsequence(s, k), 5)
s = "00101001"
k = 1
test(sol.longestSubsequence(s, k), 6)
s = "0"
k = 583196182
test(sol.longestSubsequence(s, k), 1)
