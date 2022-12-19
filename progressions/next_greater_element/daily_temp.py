from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while stack:
                if temperatures[i] < temperatures[stack[-1]]:
                    ans[i] = stack[-1] - i
                    stack.append(i)
                    break
                else:
                    stack.pop()
            stack.append(i)
        return ans
