class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        prep = ''
        sign = 1
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] in ('-', '+'):
            if s[i] == '-':
                sign *= -1
            i += 1

        while i < len(s) and s[i].isdigit():
            prep += s[i]
            i += 1
        if prep == '':
            ans = 0
        else:
            ready = int(prep) * sign
            if ready > 2 ** 31 - 1:
                ans = 2 ** 31 - 1
            elif ready < - 2 ** 31:
                ans = - 2 ** 31
            else:
                ans = ready
        return ans