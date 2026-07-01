for _ in range(int(input())):
    s = input()
    odds = s.count('1') + s.count('3')
    twos = 0
    oddss = 0
    best = odds 

    for char in s:
        if char == '2':
            twos += 1
        elif char == '1' or char == '3':
            oddss += 1

        keep = twos + (odds - oddss)
        best = max(best, keep)

    print(len(s) - best)



"""
case 1
all twos before odds and all odds

case 2
have all twos and all odds after the final two
"""


