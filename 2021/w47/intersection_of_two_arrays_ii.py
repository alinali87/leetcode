class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        d2 = {}
        ans = []
        for num in nums1:
            d1[num] = d1.get(num, 0) + 1
        for num in nums2:
            d2[num] = d2.get(num, 0) + 1
        for k, v in d1.items():
            if k in d2:
                ans.extend([k] * min(v, d2[k]))
        return ans