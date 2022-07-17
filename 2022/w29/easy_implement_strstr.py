from utils.utils import test

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # s - start index in haystack
        # s can not be greater that len(haystack) - len(needle)
        # otherwise there is not enough letters from start till the end of haystack
        for s in range(len(haystack) - len(needle) + 1):
            # suppose we believe that needle fits haystack from s index
            full = True
            # let's check letter by letter that all needle letters match haystack substring from s
            for i, char in enumerate(needle):
                # if not: break this attempt and mark full as False, our assumption for this s was wrong
                if char != haystack[s + i]:
                    full = False
                    break
            # if full is still True: all the letters match, we have found the substring
            if full:
                return s
        # if we checked all the s and still have not returned, no match was found
        return -1


sol = Solution()
haystack = "hello"
needle = "ll"
test(sol.strStr(haystack, needle), 2)

haystack = "aaaaa"
needle = "bba"
test(sol.strStr(haystack, needle), -1)

haystack = "aaa"
needle = "aaaa"
test(sol.strStr(haystack, needle), -1)
