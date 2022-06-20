from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.checker = {}
        # pref#suf: idx
        for idx, w in enumerate(words):
            for i in range(1, len(w) + 1):
                pref = w[:i]
                for j in range(len(w)):
                    suffix = w[j:]
                    s = pref + '#' + suffix
                    self.checker[s] = idx

    def f(self, prefix: str, suffix: str) -> int:
        s = prefix + '#' + suffix
        return self.checker.get(s, -1)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)