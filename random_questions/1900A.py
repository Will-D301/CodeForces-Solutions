t = int(input())
for _ in range(t):
    _ = input()
    n = input()
    before = False
    res = 0
    if len(n) <= 2:
        print(n.count("."))
        continue
    n1 = n.split("#")
    print(any([len(a) >= 3 for a in n1]))
    if any([len(a) >= 3 for a in n1]):
        print("2")
    else:
        print(n.count("."))
