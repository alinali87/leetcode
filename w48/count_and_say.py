# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"


def countAndSay(n: int) -> str:
    if n == 1:
        return '1'
    if n == 2:
        return '11'
    s = countAndSay(n - 1)
    counter = 1
    s_new = ''

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            counter += 1
        else:
            s_new += str(counter) + s[i - 1]
            counter = 1
    s_new += str(counter) + s[i]

    return s_new

print(countAndSay(4))