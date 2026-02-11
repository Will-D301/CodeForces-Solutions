for _ in range(int(input())):
    _, q = [int(a) for a in input().split()]
    a = [int(c) for c in input().split()]
    b = [int(c) for c in input().split()]
    lr = []
    for _ in range(q):
        lr.append([int(c) for c in input().split()])
    res = []
    while a:
        ma, mb = max(a), max(b)
        if ma > mb:
            mi = a.index(ma) + 1
        else:
            ma = mb
            mi = b.index(ma) + 1

        res += [ma] * mi
        b = b[mi:]
        a = a[mi:]

    g = []
    for l, r in lr:
        g.append(str(sum(res[l-1:r])))
    print(" ".join(g))
