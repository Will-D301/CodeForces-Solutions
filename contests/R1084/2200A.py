for _ in range(int(input())):
    def checkWinner(a, n, i):
        while sum(a) > 0:
            if a[i] > 0:
                a[i] -= 1

            i = (i + 1) % n
        return i


    n = int(input())
    a = [int(b) for b in input().split()]

    res = set()
    for i in range(len(a)):
        res.add(checkWinner(a.copy(), n, i))

    print(len(res))
