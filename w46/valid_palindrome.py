class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = ''
        for letter in s:
            if letter.isalnum():
                alphanum += letter.lower()
        for i in range(len(alphanum) // 2):
            if alphanum[i] != alphanum[-1 - i]:
                return False
        return True