from collections import Counter
for _ in range(int(input())):

    n = int(input())
    s = input()
    if n == 1:
        print("no")
        continue

    initial = ""
    skip = False
    for i in range(n - 1):
        if skip:
            skip = False
            continue
        if s[i] == s[i+1]:
            initial += "**"
            skip = True
        else:
            initial += s[i]

    if not skip:
        initial += s[-1]

    stack = []
    yes = False
    for ele in initial:
        if ele == "*":
            yes = True
            continue
        elif not stack:
            stack.append(ele)
            yes = False
        elif yes and stack[-1] == ele:
            stack.pop()
        else:
            stack.append(ele)

    if len(stack):
        print("no")
    else:
        print("yes")
