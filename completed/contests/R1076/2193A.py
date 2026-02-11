for _ in range(int(input())):
    _, s, x = [int(a) for a in input().split()]
    n = [int(a) for a in input().split()]
    sta = sum(n)
    a = False
    while sta <= s:
        if sta == s:
            a = True
            print("yes")
            break
        sta += x

    if not a:
        print("no")



