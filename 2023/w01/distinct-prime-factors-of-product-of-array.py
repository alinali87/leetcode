from typing import List


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def primes(n) -> list[int]:
            """
            Return list of prime numbers <= n
            """
            a = [i for i in range(n + 1)]
            a[0] = a[1] = False
            for i in range(2, n + 1):
                if i:
                    for j in range(2 * i, n + 1, i):
                        a[j] = False
            return [p for p in a if p]

        primes1000 = primes(1000)
        number = 1
        for num in nums: number *= num

        facts = set()
        for p in primes1000:
            if number % p == 0:
                facts.add(p)
        return len(facts)
