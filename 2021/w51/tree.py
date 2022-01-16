tree = [1, 3, 5, 0, 8, 9]  # array of values

def get(t, l, r, L, R):
    global tree
    if L >= r:
        return 0
    if R < l:
        return 0
    if L > l and R <= r:
        return tree[t]
    m = (R + L) // 2
    return get(2 * t + 1, l, m, L, R) + get(2 * t + 2, m, r,  L, R)


get(0, l, r, L, R)

