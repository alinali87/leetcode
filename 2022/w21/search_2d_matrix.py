from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


def test():
    s = Solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],[18, 21, 23, 26, 30]]
    target = 5
    a = s.searchMatrix(matrix, target)
    assert a is True
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],[18, 21, 23, 26, 30]]
    target = 20
    a = s.searchMatrix(matrix, target)
    assert a is False
    matrix = [[1,1]]
    target = 2
    a = s.searchMatrix(matrix, target)
    assert a is False
