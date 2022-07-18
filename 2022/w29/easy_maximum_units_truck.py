from typing import List

from utils.utils import test


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        s_box_types = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        i = 0
        units = 0
        while truckSize > 0 and i < len(boxTypes):
            box_increment = min(truckSize, s_box_types[i][0])
            units += box_increment * s_box_types[i][1]
            truckSize -= box_increment
            i += 1
        return units


sol = Solution()
boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
test(sol.maximumUnits(boxTypes, truckSize), 8)

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
test(sol.maximumUnits(boxTypes, truckSize), 91)

boxTypes = [[5,10]]
truckSize = 1
test(sol.maximumUnits(boxTypes, truckSize), 10)

boxTypes = [[1,3], [2,5]]
truckSize = 100
test(sol.maximumUnits(boxTypes, truckSize), 13)
