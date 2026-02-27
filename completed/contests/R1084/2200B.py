for _ in range(int(input())):
    n = int(input())
    a = [int(b) for b in input().split()]

    if sorted(a) == a:
        print(n)
    else:
        print("1")

