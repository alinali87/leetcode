def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        lst = list(map(int, f.readline().strip().split(' ')))
    res = 0
    for i in range(n - 2, -1, -1):
        diff = lst[i + 1] - lst[i]
        if diff < 0:
            return -1
        res += diff
    return res


if __name__ == '__main__':
    print(main())
