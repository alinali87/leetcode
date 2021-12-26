class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend >= 0 and divisor > 0:
            sign = 1
        elif dividend < 0 and divisor < 0:
            sign = 1
        else:
            sign = -1
        nom = abs(dividend)
        denom = abs(divisor)
        counter = 0
        while nom - denom >= 0:
            counter += 1
            nom -= denom
        return counter * sign