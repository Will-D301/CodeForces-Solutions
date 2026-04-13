for _ in range(int(input())):
    x = int(input())
    res = 0

    for i in range(x, x + 91):
        digitSum = sum([int(a) for a in str(i)])
        if i - digitSum == x:
            res += 1

    print(res)
