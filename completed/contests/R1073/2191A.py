t = int(input())
for _ in range(t):
    _ = input()
    a = [int(a) for a in input().split()]
    d = {}
    b = False
    for i in a:
        if b:
            d[i] = True
        else:
            d[i] = False
        b = not b
    b = d[sorted(a)[0]]
    y = False
    for i in sorted(a):
        if d[i] != b:
            print("No")
            y = True
            break
        b = not b

    if not y:
        print("Yes")
