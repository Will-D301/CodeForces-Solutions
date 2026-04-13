for _ in range(int(input())):
    n,k,p,m = [int(a) for a in input().split()]

    cards = [int(a) for a in input().split()]

    p -= 1
    winc = cards[p]
    res = 0
    n -= 1
    k -= 1
    while m > 0 and m >= winc:
        playable = cards[:k + 1]
        if p <= k:
            res += 1
            m -= winc
            cc = p
            p = n
        else:
            mi = min(playable)
            m -= mi
            cc = cards.index(mi)
            p -= 1

        cards += [cards.pop(cc)]

    print(res)

