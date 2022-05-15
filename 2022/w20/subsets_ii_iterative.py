from typing import List


class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
             we will sort your return value in output
    """
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        def get_subsets(num, sets):
            new_sets = set()
            for s in sets:
                new_s = tuple(sorted(s + (num,)))
                new_sets.add(new_s)
            sets.update(new_sets)
            return sets

        ans = {tuple()}
        for num in nums:
            ans = get_subsets(num, ans)
        return sorted(ans)
