# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e762e
def calc_num(s):
    total = sum([int(num) for num in s])
    add = 9 - total % 9
    if add == 9:
        add = 0
    for i, num in enumerate(s):
        if add == 0 and i == 0:
            continue
        if add < int(num):
            return s[:i] + str(add) + s[i:]
    return s + str(add)

n = int(input())
for i in range(n):
    print(f"Case #{i + 1}: {calc_num(input())}")




