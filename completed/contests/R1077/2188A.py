for _ in range(int(input())):
    n = int(input())
    b = True
    if n % 2:
        a = [2, 3, 1]
        b = False
    else:
        a = [1, 2]



    for i in range(len(a) + 1, n, 2):
        if not b:
            a = [x + 1 for x in a] + [i+1, 1]
        else:
            a = [x + 1 for x in a] + [1, i + 1]


    print(" ".join([str(x) for x in a]))
