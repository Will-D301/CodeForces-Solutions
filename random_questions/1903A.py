test = input()
for _ in range(int(test)):
    t, k = input().split()
    t = int(t)
    k = int(k)
    n = input().split()
    n = [int(a) for a in n]
    if sorted(n) == n:
        print("yes")
    elif k >= 2:
        print("yes")
    else:
        print("no")
