class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(len(board))]
        for i in range(len(board)):
            row = set()
            for j in range(len(board[0])):
                if board[i][j].isdigit():
                    digit = int(board[i][j])
                    if digit in row or digit in cols[j]:
                        return False
                    row.add(digit)
                    cols[j].add(digit)
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j].isdigit():
                    digit = int(board[i][j])
                    if digit in squares[i // 3][j // 3]:
                        return False
                    squares[i // 3][j // 3].add(digit)
        return True