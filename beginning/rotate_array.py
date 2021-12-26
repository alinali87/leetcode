class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        tail = nums[-k:]
        head = nums[:-k]
        new_nums = tail + head
        for i in range(len(nums)):
            nums[i] = new_nums[i]


s = Solution()
with open('input.txt') as file:
    nums = list(map(int, file.readline().rstrip()[1:-1].split(',')))
    k = int(file.readline().rstrip())
s.rotate(nums, k)
print(nums)

