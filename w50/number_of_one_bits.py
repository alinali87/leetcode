def hammingWeight(n: int) -> int:
    s = bin(n).replace('0b', '')
    counter = 0
    for letter in s:
        if letter == '1':
            counter += 1
    return counter

ans = hammingWeight(10)
print(type(ans))
print(ans)