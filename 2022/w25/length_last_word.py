

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        is_letter = False
        counter = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and is_letter:
                break
            if s[i] == ' ':
                continue
            if s[i].isalpha():
                is_letter = True
                counter += 1
        return counter

    def lengthOfLastWordShort(self, s: str) -> int:
        splitted = s.split()
        return len(splitted[-1])


def test():
    sol = Solution()
    s = "Hello World"
    assert sol.lengthOfLastWord(s) == 5

    s = "   fly me   to   the moon  "
    assert sol.lengthOfLastWord(s) == 4

    s = "luffy is still joyboy"
    assert sol.lengthOfLastWord(s) == 6


test()
