for _ in range(int(input())):
    x = int(input())
    res = 0
    c = str(x).removeprefix('9')

    if c and int(c) == 0:
        print(0)


    elif not x % 9:
        print(10)

    else:
        print(0)
