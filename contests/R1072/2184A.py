t = int(input())
for _ in range(t):
    n = int(input())
    if n == 2:
        print("2")
        continue
    if n == 3:
        print("3")
        continue
    if not n % 2:
        print("0")
    else:
        print("1")
