test = int(input())
for _ in range(test):
    n = int(input())
    if n == 1:
        print(1)
        continue
    if n == 2:
        print(9)
        continue
    a = n**2
    if 3 <= n <= 4:
        print(4*a - n - 4)
        continue
    print(5 * a - 5 * n - 5)
