for _ in range(int(input())):
    n = int(input())
    a = [int(b) for b in input().split()]
 
    res = []
    for i in range(n - 1):
        num = a[i]
        nl = 0
        ng = 0
        for j in range(i + 1, n):
            if a[j] > num:
                nl += 1
            elif a[j] < num:
                ng += 1
 
        res.append(max(nl, ng))
    res.append(0)
    print(" ".join([str(b) for b in res]))
