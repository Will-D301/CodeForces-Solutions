a = int(input())
for _ in range(a):
    n, x = input().split()
    n, x = int(n), int(x)
    b = input().split()
    b = [0] + [int(c) for c in b]
    m = 2 * (x - b[-1])
    for i in range(1, len(b)):
        if b[i] - b[i-1] > m:
            m = b[i] - b[i-1]
    print(m)
