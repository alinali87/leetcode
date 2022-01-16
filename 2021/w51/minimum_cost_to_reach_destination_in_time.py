from collections import defaultdict
from heapq import (heappop, heappush)
from typing import List


class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        heap = [(passingFees[0], 0, 0)]  # (cost, time, curr)
        nodeToTime = {}

        edgesDict = defaultdict(list)
        for a, b, time in edges:
            edgesDict[a].append((b, time))
            edgesDict[b].append((a, time))

        while heap:
            cost, time, curr = heappop(heap)

            if time > maxTime:
                continue

            if curr == n - 1:
                return cost

            # No point in visting this node again if it was visited before with a lower cost AND lower time.
            if curr not in nodeToTime or nodeToTime[curr] > time:

                nodeToTime[curr] = time

                for nextNode, travelTime in edgesDict[curr]:
                    heappush(heap, (cost + passingFees[nextNode], time + travelTime, nextNode))

        return -1
