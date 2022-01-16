def strStr(haystack: str, needle: str) -> int:
    if needle == '':
        return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack) - len(needle) + 1):
        match = True
        for offset in range(len(needle)):
            if needle[offset] != haystack[i + offset]:
                match = False
                break
        if match == True:
            return i
    return -1

def str_str(haystack: str, needle: str) -> int:
    if needle == '':
        return 0
    if len(needle) > len(haystack):
        return -1
    return haystack.find(needle)

with open('input.txt') as file:
    a = file.readline().rstrip()
    b = file.readline().rstrip()

print(strStr(a, b))