from utils.utils import test


class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10 ** 9 + 7
        def fib(n, m):
            if n == 1 or n == 0:
                return 1
            else:
                a, b = 1, 1
                for i in range(1, n):
                    a, b = b, (a + b) % m
                return (b * b) % m
        return fib(n + 1, mod)


sol = Solution()
n = 1000
test(sol.countHousePlacements(n), 500478595)
