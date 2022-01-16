class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        tail = nums[-k:]
        head = nums[:-k]
        new_nums = tail + head
        for i in range(len(nums)):
            nums[i] = new_nums[i]