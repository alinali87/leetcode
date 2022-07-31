from utils.utils import test


class Solution:
    def isPalindrome(self, s: str) -> bool:
        def process_char(char) -> s:
            if char.isalnum():
                return char.lower()
            return ''
        l, r = 0, len(s) - 1
        while l < r:
            left = process_char(s[l])
            if not left:
                l += 1
                continue
            right = process_char(s[r])
            if not right:
                r -= 1
                continue
            if left != right:
                return False
            else:
                l += 1
                r -= 1
        return True


sol = Solution()
s = "A man, a plan, a canal: Panama"
test(sol.isPalindrome(s), True)

s = "race a car"
test(sol.isPalindrome(s), False)
