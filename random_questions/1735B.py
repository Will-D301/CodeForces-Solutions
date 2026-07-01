for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    mi = min(a) 
    midiff = mi * 2 - 1
    res = 0
    for num in a:
        res += (num - 1) // midiff
    print(res)
    
