def romanToInt(s: str) -> int:
    digits = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    pairs = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    i = 0
    num = 0
    while i < len(s):
        if i < len(s) - 1:
            if s[i] + s[i + 1] in pairs:
                num += pairs[s[i] + s[i + 1]]
                i += 2
            else:
                num += digits[s[i]]
                i += 1
        else:
            num += digits[s[i]]
            i += 1
    return num

print(romanToInt("MCDXXVIII"))