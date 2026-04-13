
for _ in range(int(input())):
    n, m = [int(a) for a in input().split()]
    a = [int(a) for a in input().split()]


    counter = 1
    y = True

    for i in range(1, n):
        if a[i] == a[i - 1]:
            counter += 1
            if counter >= m:
                y = False
                break
        else:
            counter = 1

    if y:
        print("yes")
    else:
        print("no")


