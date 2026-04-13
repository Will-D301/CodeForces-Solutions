for _ in range(int(input())):
    n, c, k = [int(a) for a in input().split()]
    a = sorted([int(b) for b in input().split()])

    for ele in a:
        if ele <= c:
            b = c - ele
            if b >= k:
                c += k
                k = 0
            else:
                c += b
                k -= b
            c += ele

    print(c)
