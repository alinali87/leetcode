from collections import defaultdict
from typing import List
from utils.utils import test


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        # key - type of task, value - index last time it was seen
        last_seen = defaultdict(lambda: -float('inf'))
        day = 0
        for i, t in enumerate(tasks):
            day = max(day + 1, last_seen[t] + space + 1)
            last_seen[t] = day
        return day


sol = Solution()
tasks = [1,2,1,2,3,1]
space = 3
test(sol.taskSchedulerII(tasks, space), 9)

tasks = [4,10,10,9,10,4,10,4]
space = 8
test(sol.taskSchedulerII(tasks, space), 30)
