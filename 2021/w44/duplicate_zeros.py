class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                for k in range(len(arr) - 2, i, -1):
                    arr[k + 1] = arr[k]
                arr[i + 1] = 0
                i += 2
            else:
                i += 1
