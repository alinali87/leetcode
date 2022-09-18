from typing import List
from utils.utils import test


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        worst_order = sorted(transactions, key=lambda x: (1 if x[1] - x[0] >= 0 else 0, -x[0] if x[1] - x[0] >= 0 else x[1]))
        cummin = 0
        acc = 0
        for pair in worst_order:
            acc = acc - pair[0]
            cummin = min(cummin, acc)
            acc = acc + pair[1]
        if cummin < 0:
            return -cummin
        return 0


sol = Solution()
tr = [[5,0], [4,2], [2,1]]
test(sol.minimumMoney(tr), 10)
tr = [[3,9],[0,4],[7,10],[3,5],[0,9],[9,3],[7,4],[0,0],[3,3],[8,0]]
test(sol.minimumMoney(tr), 24)