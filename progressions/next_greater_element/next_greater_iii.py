class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        if len(nums) < 2:
            return -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                nums = nums[:i + 1] + sorted(nums[i + 1:])
                break
        x = int(''.join(nums))
        if x > 2 ** 31 - 1:
            return -1
        if x > n:
            return x
        return -1
