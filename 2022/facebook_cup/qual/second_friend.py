def solution():
    ans = []
    with open('input.txt') as f:
        t = int(f.readline())
        for i in range(t):
            trees = 0
            r, c = map(int, f.readline().split(' '))
            for _ in range(r):
                line = f.readline()
                trees += line.count('^')
            if (r == 1 or c == 1) and trees > 0:
                ans.append(f'Case #{i + 1}: Impossible')
            elif (r == 1 or c == 1) and trees == 0:
                picture = '\n'.join('.' * c for _ in range(r))
                ans.append(f'Case #{i + 1}: Possible\n{picture}')
            else:
                picture = '\n'.join('^' * c for _ in range(r))
                ans.append(f'Case #{i + 1}: Possible\n{picture}')
    with open('output.txt', 'w') as f:
        f.write('\n'.join(ans))


if __name__ == '__main__':
    solution()
