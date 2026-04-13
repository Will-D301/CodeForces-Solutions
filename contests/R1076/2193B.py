for _ in range(int(input())):
    _ = input()
    n = [int(a) for a in input().split()]
    res = []
    while n.index(max(n)) == 0:
        res.append(n[0])
        n = n[1:]
        if not n:
            break


    if not n:
        print(" ".join([str(a) for a in res]))
        continue
    mi = n.index(max(n))
    res.extend(n[0:mi + 1][::-1])
    res.extend(n[mi + 1:])
    print(" ".join([str(a) for a in res]))
