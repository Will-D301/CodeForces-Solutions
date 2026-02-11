t = int(input())
for _ in range(t):
    s, k, m = input().split()
    s, k, m = int(s), int(k), int(m)
    if not m % k:
        print(min(s, m))
        continue

    minsBefore = m % k
    minsLeft = max(min(m - minsBefore, s - minsBefore), 0)
    if s < minsLeft:
        print(0)
    else:
        print(minsLeft)
