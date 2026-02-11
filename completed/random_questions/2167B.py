n = int(input())
for _ in range(n):
  _ = input()
  a, b = input().split()
  if sorted(a) == sorted(b):
    print("Yes")
  else:
    print("No")
