for _ in range(int(input())):
    n = int(input())
    s = input()
    old = s
    while True:
        new = old[0]
        for i in range(1, n - 1):
            if old[i-1] == '1' and old[i+1] == '1':
                new += '1'
            else:
                new += old[i]

        new += old[-1]
        if old == new:
            break
        else:
            old = new
    ma = old.count('1')

    while True:
        new = old[0]
        for i in range(1, n - 1):
            if old[i-1] == '1' and old[i+1] == '1' and old[i] == '1':
                new += '0'
                new += old[i + 1:n - 1]
                break

            else:
                new += old[i]

        new += old[-1]
        if old == new:
            break
        else:
            old = new


    print(f"{old.count('1')} {ma}")
