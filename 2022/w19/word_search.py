from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if board[i][j] == word[k]:
                check[i][j] = 1
                if k == word_length - 1:
                    return True
                k += 1
                for d in dirs:
                    if 0 <= i + d[0] <= height - 1 and 0 <= j + d[1] <= width - 1:
                        if check[i + d[0]][j + d[1]] == 1:
                            continue
                        res = dfs(i + d[0], j + d[1], k)
                        if res:
                            return True
                check[i][j] = 0
            else:
                return False
            return False

        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        height = len(board)
        width = len(board[0])
        word_length = len(word)
        check = [[0 for _ in range(width)] for _ in range(height)]

        for i in range(height):
            for j in range(width):
                k = 0
                res = dfs(i, j, k)
                if res:
                    return True
            check[i][j] = 0
        return False
