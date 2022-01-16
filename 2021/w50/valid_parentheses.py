class Solution:
    def isValid(self, s: str) -> bool:
        opens = ['(', '[', '{']
        match = {'(': ')', '[': ']', '{': '}'}
        stack = []
        i = 0
        while i < len(s):
            par = s[i]
            if par in opens:
                stack.append(par)
            elif not stack:
                return False
            else:
                a = stack.pop()
                if match[a] != par:
                    return False
            i += 1
        if len(stack) > 0:
            return False
        return True