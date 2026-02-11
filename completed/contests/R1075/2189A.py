t = int(input())
for _ in range(t):
    a = [int(a) for a in input().split()]
    h, l = a[1], a[2]
    n = [int(a) for a in input().split()]
    res = 0
    lF = []
    hF = []
    bF = []
    for num in n:
        if num <= h and num <= l:
            bF.append(n)
        elif num <= h:
            hF.append(n)
        elif num <= l:
            lF.append(n)

    for num in lF:
        if hF:
            hF.pop()
            res += 1
        elif bF:
            bF.pop()
            res += 1
        else:
            break

    for num in hF:
        if bF:
            bF.pop()
            res += 1

    res += len(bF) // 2

    print(res)
