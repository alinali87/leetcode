from typing import List

def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    zeros = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zeros.append((i, j))

    def replace_to_zeros(i, j, matrix):
        for col in range(len(matrix[i])):
            matrix[i][col] = 0
        for row in range(len(matrix)):
            matrix[row][j] = 0

    for i, j in zeros:
        replace_to_zeros(i, j, matrix)

