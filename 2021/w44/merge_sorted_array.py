class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        buf = []
        i = 0
        j = 0
        while i <= m and j <= n:
            # if nums1[i] == 0 and j == n:
            #     break
            # elif nums1[i] == 0 and j < n:
            #     buf.append(nums2[j])
            #     j += 1
            # elif nums1[i] != 0 and j == n:
            #     buf.append(nums1[i])
            #     i += 1
            if j < n and i < m:
                if nums1[i] <= nums2[j]:
                    buf.append(nums1[i])
                    i += 1
                else:
                    buf.append(nums2[j])
                    j += 1
            elif i < m:
                buf.append(nums1[i])
                i += 1
            elif j < n:
                buf.append(nums2[j])
                j += 1
            else:
                break
        if len(buf) == m + n:
            for k in range(m + n):
                nums1[k] = buf[k]



