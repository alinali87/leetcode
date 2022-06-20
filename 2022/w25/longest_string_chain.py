from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda x: len(x))
        voc = {}
        for w in words:
            for pos in range(len(w)):
                prev = w[:pos] + w[pos + 1:]
                c = voc.get(prev, 0) + 1
                voc[w] = max(c, voc.get(w, 0))
        return max(voc.values())


def test(a, b):
    assert a == b


sol = Solution()

words = ["a","b","ba","bca","bda","bdca"]
test(sol.longestStrChain(words), 4)

words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
test(sol.longestStrChain(words), 5)

words = ["abcd","dbqca"]
test(sol.longestStrChain(words), 1)
