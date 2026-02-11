for _ in range(int(input())):
    _ = int(input())
    a = input()
    a = [int(x) for x in a]
    if len(a) == 1:
        print(1)
        continue
    if len(a) == 2:
        no = a[0] + a[1]
        if not no:
            print(1)
        else:
            print(no)
        continue
    no = a[0]

    res = []

    o = True
    for i in range(len(a) - 1):
        if a[i]:
            no += 1
            o = True
            h = 1
        elif not o and not a[i + 1]:
            no += 1
            o = True
            h = 1
        else:
            o = False
            h = 0

        res.append(h)

    res.append(a[-1])
    if not res[0] and not res[1]:
        no += 1
    if not res[-1] and not res[-2]:
        no += 1

    no2 = a[-1]

    res2 = []

    o = True
    for i in range(len(a) - 1, 0, -1):
        if a[i]:
            no2 += 1
            o = True
            h = 1
        elif not o and not a[i - 1]:
            no2 += 1
            o = True
            h = 1
        else:
            o = False
            h = 0

        res2.append(h)

    res2.append(a[0])
    if not res2[0] and not res2[1]:
        no2 += 1
    if not res2[-1] and not res2[-2]:
        no2 += 1


    print(min(no, no2))


