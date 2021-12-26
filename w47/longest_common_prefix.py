class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        min_str = min(strs, key=lambda x: len(x))
        if len(min_str) == 0:
            return prefix
        for i in range(len(min_str)):
            sym = min_str[i]
            for word in strs:
                if word[i] != sym:
                    return prefix
            prefix += min_str[i]
        return prefix