from typing import List


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []

        for q in queries:
            l = 0
            while q[1] != q[0]:
                if q[1] < q[0]:
                    l += 1
                    if q[0] % 2 == 0:
                        q[0] /= 2
                    else:
                        q[0] = (q[0] - 1) / 2
                else:
                    l += 1
                    if q[1] % 2 == 0:
                        q[1] /= 2
                    else:
                        q[1] = (q[1] - 1) / 2
            ans.append(l + 1)
        return ans
