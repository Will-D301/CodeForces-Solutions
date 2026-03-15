

for _ in range(int(input())):

    dic = dict()

    n = int(input())
    res = []

    for i in range(n):
        res.append([int(a) for a in input().split()])

    if n == 1:
        print("no")
        continue

    for ele in res:
        for e in ele:
            if e not in dic:
                dic[e] = 1
            else:
                dic[e] += 1

    ma = 0

    for key in dic:
        ma = max(ma, dic[key])


    if ma > (n**2 - n):
        print("no")
    else:
        print("yes")
