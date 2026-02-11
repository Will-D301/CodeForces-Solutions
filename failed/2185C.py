t = int(input())
for _ in range(t):
    _ = input()
    a = [int(a) for a in input().split()]
    a = list(set(a))
    a = sorted(a)
    a = [b-a[0] for b in a]
    y = False
    for i in range(len(a)):
        if i != a[i]:
            ans = i
            y = True
            break
    if not y:
        print(len(a))
