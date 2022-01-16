class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n > 1:
            if n % 3 == 0:
                n = n // 3
            else:
                return False
        return True

s = Solution()
def test10():
    ans = s.isPowerOfThree(10)
    assert ans == False


def test9():
    ans = s.isPowerOfThree(9)
    assert ans is True


def test81():
    ans = s.isPowerOfThree(81)
    assert ans == True


test10()
test9()
test81()

