from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nm = [[None for _ in range(len(matrix))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                nm[j][-1 - i] = matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = nm[i][j]
