for _ in range(int(input())):
    s, t = input().split()
    l = len(t)
    revs = reversed(s)
    revt = list(reversed(t))
    counter = 0
    got = []
    y = True
    for char in revs:
        if counter == l:
            print("yes")
            y = False
            break
        if char == revt[counter]:
            counter += 1
            got.append(char)
        elif char in revt[counter:]:
            print("no")
            y = False
            break
    if counter == l and y:
        print("yes")
    if counter != l and y:
        print("no") 
