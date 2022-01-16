class Solution:
    def firstUniqChar(self, s: str) -> int:
        idx = []
        u_letters = set()
        d_letters = set()
        for i in range(len(s)):
            if s[i] in u_letters:
                u_letters.remove(s[i])
                d_letters.add(s[i])
            elif s[i] in d_letters:
                continue
            else:
                u_letters.add(s[i])
                idx.append(i)
        for i in idx:
            if s[i] in u_letters:
                return i
        return -1


