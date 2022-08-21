# brute force solution, TODO: solve in O(n)
from utils.utils import test


class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        if len(s) == 1:
            return 0
        counter = -1
        prev = 0
        curr = 1
        s = list(s)
        new_s = []
        while True:
            counter += 1
            swap = 0
            while curr < len(s):
                if s[prev] == '0' and s[curr] == '1':
                    swap += 1
                    new_s.append('1')
                    new_s.append('0')
                    prev += 2
                    curr += 2
                else:
                    new_s.append(s[prev])
                    prev += 1
                    curr += 1
            if prev < len(s):
                new_s.append(s[prev])
            if swap == 0:
                return counter
            s = new_s
            new_s = []
            prev = 0
            curr = 1


sol = Solution()
s = "0110101"
test(sol.secondsToRemoveOccurrences(s), 4)
s = "11100"
test(sol.secondsToRemoveOccurrences(s), 0)
