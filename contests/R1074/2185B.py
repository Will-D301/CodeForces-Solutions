t = int(input())
for _ in range(t):
    _ = int(input())
    a = [int(a) for a in input().split()]
    print(max(a) * len(a))


