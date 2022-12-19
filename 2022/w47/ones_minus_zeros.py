from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        zeros_row = [0] * len(grid)
        ones_row = [0] * len(grid)
        zeros_col = [0] * len(grid[0])
        ones_col = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    zeros_row[i] += 1
                    zeros_col[j] += 1
                else:
                    ones_row[i] += 1
                    ones_col[j] += 1
        diff = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]
        return diff


s = Solution()
grid = [[1,1,1],[1,1,1]]
d = s.onesMinusZeros(grid)
print(d)