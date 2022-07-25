# TODO refactor
from typing import List

from utils.utils import test


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        class Node:
            def __init__(self):
                self.is_terminal = 0
                self.links = {}

        def add_string(root: Node, string):
            curr_node = root
            for i in range(len(string)):
                symbol = string[i]
                if symbol not in curr_node.links:
                    new_node = Node()
                    curr_node.links[symbol] = new_node
                curr_node = curr_node.links[symbol]
            curr_node.is_terminal = 1
            return

        def build_trie(strings: list):
            root = Node()
            for string in strings:
                add_string(root, string)
            return root

        def main(text: str, strings: list):
            root = build_trie(strings)
            if text[0] not in root.links:
                return 0
            # 1 - можно разложить строку на слова, 0 - нельзя
            dp = [0 for _ in range(len(text))]
            # начинаем поиск слова с позиции в тексте = starter
            starters = [0]
            # уже добавленные позиции заносим в множество и их больше не проверяем
            added = {0}
            # с помощью head двигаемся по массиву starters
            head = 0
            while head < len(starters):
                starter = starters[head]
                current_node = root
                offset = 0
                mismatch_not_found = True
                while mismatch_not_found and (starter + offset) < len(text):
                    symbol = text[starter + offset]
                    if symbol in current_node.links:
                        current_node = current_node.links[symbol]
                        if current_node.is_terminal == 1:
                            dp[starter + offset] = 1
                            if starter + offset + 1 not in added:
                                starters.append(starter + offset + 1)
                                added.add(starter + offset + 1)
                        offset += 1
                    else:
                        mismatch_not_found = False
                head += 1
            return dp[-1]

        ans = main(s, wordDict)
        if ans == 1:
            return True
        else:
            return False

sol = Solution()
s = "leetcode"
wordDict = ["leet","code"]
test(sol.wordBreak(s, wordDict), True)
