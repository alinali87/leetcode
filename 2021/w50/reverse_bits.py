
class Solution:
    def reverseBits1(self, n: int) -> int:
        x_str = bin(n).replace('0b', '')
        x_str = "0" * (32 - len(x_str)) + x_str
        x_reversed = ''.join(reversed(x_str))
        return int(x_reversed, base=2)

    def reverseBits(self, n: int) -> int:
        x = list(bin(n).replace('0b', ''))
        ans = 0
        for i in range(len(x)):
            ans += int(x[-1 - i]) * 2 ** (31 - i)
        return ans

    def rb(self, n):
        num = bin(n)
        return int(('0' * (36 - len(num) - 2) + num[2:])[::-1], base=2)


# s = Solution()
# ans = s.reverseBits(43261596)
# print(ans)

a = "asdfghjkl"
n = 3
print(a[:1:-1])