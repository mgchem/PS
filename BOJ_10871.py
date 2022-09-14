import sys
n, x = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
s = ""
for i in data:
    if i < x:
        s += str(i)
        s += " "
print(s[:-1])
