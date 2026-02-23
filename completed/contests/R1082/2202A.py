for _ in range(int(input())):
    x, y = [int(a) for a in input().split()]
    currx = curry = 0
    if y > 0:
        currx += 2 * y
    elif y < 0:
        currx += 4 * abs(y)

    curry = y

    if currx > x:
        print("no")
    elif not (x - currx) % 3:
        print("yes")
    else:
        print("no")
