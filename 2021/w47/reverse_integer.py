class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        if x[0] == '-':
            reversed_x = ['-']
        else:
            reversed_x = []
        for i in range(len(x) - 1, len(reversed_x) - 1, -1):
            reversed_x.append(x[i])
        reversed_x = ''.join(reversed_x)
        reversed_x = int(reversed_x)
        if reversed_x > 2 ** 31 - 1 or reversed_x < -2 ** 31:
            return 0
        else:
            return reversed_x