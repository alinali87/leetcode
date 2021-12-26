class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_str = bin(x).replace('0b', '')
        y_str = bin(y).replace('0b', '')
        x_str = '0' * (32 - len(x_str)) + x_str
        y_str = '0' * (32 - len(y_str)) + y_str
        counter = 0
        for i in range(32):
            if x_str[i] != y_str[i]:
                counter += 1
        return counter
