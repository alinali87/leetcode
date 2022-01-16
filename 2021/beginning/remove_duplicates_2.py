class Solution:
    def removeDuplicates(self, nums: list) -> int:
        k = len(nums) - 1
        if k == 0:
            return k + 1
        i = 1
        while i < k:
            if nums[i] <= nums[i - 1]:
                j = i + 1
                k -= 1
                while nums[j] <= nums[i] and i < k:
                    j += 1
                    k -= 1
                nums[i] = nums[j]
            i += 1
        # if nums[k] <= nums[k - 1]:
        #     k -= 1
        return k + 1


s = Solution()
file = open('input.txt')
nums = list(map(int, file.readline().rstrip()[1:-1].split(',')))
file.close()
k = s.removeDuplicates(nums)
print("k:", k)
print("nums:", nums)