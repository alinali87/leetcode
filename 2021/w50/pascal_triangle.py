

class Solution:
    def generate(numRows: int):
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        ans = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            prev = ans[i - 1]
            for k in range(1, len(prev)):
                row.append(prev[k] + prev[k - 1])
            row.append(1)
            ans.append(row)
        return ans

