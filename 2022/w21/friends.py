from typing import List
import math


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = 0
        ages = sorted(ages)
        counts = [0] * 121   # 0 .. 120
        for age_max in ages:
            age_min = math.floor(0.5 * age_max + 7) + 1
            for age in range(age_min, age_max + 1):
                if age == age_max:
                    # each person with age == age can send request to this person
                    # and this person can send request to each person of age == age
                    count += 2 * counts[age]
                else:
                    count += counts[age]
            counts[age_max] += 1
        return count


def test():
    s = Solution()
    ages = [20, 30, 100, 110, 120]  # 3
    a = s.numFriendRequests(ages)
    assert a == 3
    ages = [16,17,18]  # 2
    a = s.numFriendRequests(ages)
    assert a == 2
    ages = [16, 16] # 2
    a = s.numFriendRequests(ages)
    assert a == 2
