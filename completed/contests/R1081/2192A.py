for _ in range(int(input())):
    n = int(input())
    s = input()

    def num_of_blocks(s):
        amt = 1
        c = s[0]
        for char in s[1:]:
            if char != c:
                amt += 1
                c = char
        return amt

    m = 0
    for i in range(n):
        m = max(num_of_blocks(s[-i:] + s[:-i]), m)

    print(m)
