# tag: recursion
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = []
        if digits == '':
            return result
        def get_combinations(prefix, n):
            if n == len(digits):
                result.append(prefix)
            else:
                for l in d[digits[n]]:
                    get_combinations(prefix + l, n + 1)
        get_combinations('', 0)
        return result
