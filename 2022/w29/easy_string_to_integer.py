from utils.utils import test


class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        negative = False
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] in ('+', '-'):
            if s[i] == '-':
                negative = True
            i += 1
        if negative:
            num_arr = ['-']
        else:
            num_arr = []
        while i < len(s) and s[i].isdigit():
            num_arr.append(s[i])
            i += 1
        num_str = ''.join(num_arr)
        if num_str not in ('', '-'):
            num = int(num_str)
        else:
            return 0
        if num < -2 ** 31:
            return -2 ** 31
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return num



sol = Solution()
s = "42"
test(sol.myAtoi(s), 42)

s = "   -42"
test(sol.myAtoi(s), -42)

s = "4193 with words"
test(sol.myAtoi(s), 4193)

s = "4193 with words"
test(sol.myAtoi(s), 4193)

s = "2147483648"
test(sol.myAtoi(s), 2147483647)

s = "+-12"
test(sol.myAtoi(s), 0)

s = ""
test(sol.myAtoi(s), 0)
