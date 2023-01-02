class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        a = 0
        while target != startValue:
            if target < startValue:
                a = a + (startValue - target)
                return a
            elif target % 2 == 0:
                target //= 2
            else:
                target += 1
            a += 1
        return a
