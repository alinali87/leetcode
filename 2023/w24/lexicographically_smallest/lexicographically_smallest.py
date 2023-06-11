class Solution:
    def smallestString(self, s: str) -> str:
        def to_zero_base(x):
            return x - 97

        def to_97_base(code):
            return code + 97

        def shift_left(let):
            return chr(to_97_base((to_zero_base(ord(let)) - 1) % 26))

        def shift_string(s: str) -> str:
            return ''.join(shift_left(let) for let in s)

        for i, let in enumerate(s):
            if let != 'a':
                start = i
                for j, let in enumerate(s[i+1:], start=i+1):
                    if let == 'a':
                        end = j
                        break
                else:
                    end = len(s)
                return s[:start] + shift_string(s[start:end]) + s[end:]
        return s[:-1] + shift_left(s[-1])
