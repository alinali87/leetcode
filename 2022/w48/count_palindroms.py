class Solution:
    def countPalindromes(self, s: str) -> int:
        n = len(s)
        m = 10 ** 9 + 7
        pref = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(n)]
        cnts = [0] * 10

        for i in range(n):
            c = ord(s[i]) - ord('0')
            if i:
                for j in range(10):
                    for k in range(10):
                        pref[i][j][k] = pref[i - 1][j][k]
                        if k == c: pref[i][j][k] += cnts[j]
            cnts[c] += 1

        suff = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(n)]
        cnts = [0] * 10
        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - ord('0')
            if i < n - 1:
                for j in range(10):
                    for k in range(10):
                        suff[i][j][k] = suff[i + 1][j][k]
                        if k == c: suff[i][j][k] += cnts[j]
            cnts[c] += 1

        ans = 0
        for k in range(2, len(s) - 2):
            for i in range(10):
                for j in range(10):
                    ans += pref[k][i][j] * suff[k][j][i]
        return ans % m


sol = Solution()
s = "103301"
ans = sol.countPalindromes(s)
print(ans)


