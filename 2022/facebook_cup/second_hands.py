from collections import Counter


def solution():
    with open('input.txt') as f:
        t = int(f.readline())
        ans = []
        for i in range(t):
            res = 'YES'
            n, k = map(int, f.readline().split(' '))
            s = map(int, f.readline().split(' '))
            if n > 2 * k:
                res = 'NO'
            else:
                c = Counter(s)
                if c.most_common(1)[0][1] > 2:
                    res = 'NO'
            ans.append(f'Case #{i + 1}: {res}')
    with open('output.txt', 'w') as output:
        output.write('\n'.join(ans))


if __name__ == '__main__':
    solution()
