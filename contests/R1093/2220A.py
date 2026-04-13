for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    nums = set()
    y = True
    for num in a:
        if num in nums:
            print(-1)
            y = False
            break
        nums.add(num)

    if y:
        print(*sorted(a, reverse=True))
