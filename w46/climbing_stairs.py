class Solution:
    def climbStairs(self, n: int) -> int:
        seq = [1, 1]
        for i in range(2, n + 1):
            seq.append(seq[i - 1] + seq[i - 2])
        return seq[n]
