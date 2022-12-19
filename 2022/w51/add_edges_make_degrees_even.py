from typing import List


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        gr = [[] for _ in range(n + 1)]
        for e in edges:
            gr[e[0]].append(e[1])
            gr[e[1]].append(e[0])
        # print(f'{gr=}')
        odd = []

        def exists(i, j):
            for e in gr[i]:
                if e == j:
                    return True
            return False

        for v in range(1, n + 1):
            if len(gr[v]) % 2 == 1:
                odd.append(v)
        # print(f'{odd=}')
        if len(odd) % 2 == 1 or len(odd) > 4:
            return False
        if len(odd) == 2:
            if len(gr[odd[0]]) == n - 1: return False
            if len(gr[odd[1]]) == n - 1: return False
            return True
        if len(odd) == 0:
            return True

        for i in range(4):
            badi = 0
            for j in range(4):
                if i == j:
                    continue
                if exists(odd[i], odd[j]):
                    badi += 1
            if badi == 3:
                return False

        edges1 = []
        for i in range(4):
            for j in range(i + 1, 4):
                edges1.append((i, j))

        for i in range(len(edges1)):
            for j in range(i + 1, len(edges1)):
                vv = set()
                vv.add(odd[edges1[i][0]])
                vv.add(odd[edges1[i][1]])
                vv.add(odd[edges1[j][0]])
                vv.add(odd[edges1[j][1]])
                if len(vv) != 4:
                    continue
                if not exists(odd[edges1[i][0]], odd[edges1[i][1]]) and not exists(odd[edges1[j][0]],
                                                                                   odd[edges1[j][1]]):
                    return True

        return False
