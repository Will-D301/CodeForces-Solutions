num = int(input())
for i in range(num):
    l, a, b = input().split()
    l, a, b = int(l), int(a), int(b)
    numbers = []
    while a not in numbers:
        numbers.append(a)
        a += b
        a %= l
        if a == l - 1:
            numbers.append(a)
            break
    print(str(max(numbers)))
