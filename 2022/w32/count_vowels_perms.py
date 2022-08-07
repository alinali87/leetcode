from collections import defaultdict
from utils.utils import test


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        d = {'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}
        mod = 10 ** 9 + 7
        last_letters = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

        for i in range(n - 1):
            next_letters = defaultdict(int)
            for l, count in last_letters.items():
                for option in d[l]:
                    next_letters[option] += count
            last_letters = next_letters
        return sum(last_letters.values()) % mod


sol = Solution()
n = 144
test(sol.countVowelPermutation(n), 18208803)
