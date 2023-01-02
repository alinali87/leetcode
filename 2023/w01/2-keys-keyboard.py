class Solution:
    def minSteps(self, n: int) -> int:
        # n = 1 ->
        # n = 2 -> copy + paste
        # n = 3 -> copy + p + p

        # n = 4 -> {c + p}, p

        # n = 837 // 3 = 279 (3 op)
        # 279 // 3 = 93 (3 op)
        # 93 // 3 = 31 (3 op)
        # 31 --> 31 op

        def primes(left, n):
            a = [i for i in range(n + 1)]
            a[0] = a[1] = False
            for i in range(2, n + 1):
                if a[i]:
                    for j in range(2 * i, n + 1, i):
                        a[j] = False
            return [x for x in a if x >= left and x]

        prime_list = primes(2, 1000)
        a = 0
        while n != 1:
            for p in prime_list:
                if n % p == 0:
                    a += p
                    n //= p
                    break

        return a
