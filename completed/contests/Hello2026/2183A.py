test = int(input())
for _ in range(test):
    b = input()
    a = input().split()

    if a.count("1") == len(a):
        print("alice")

    elif a[0] == "1" and "0" in a[1:]:
        print("alice")

    elif a[-1] == "1" and "0" in a[:-1]:
        print("alice")

    else:
        print("bob")
