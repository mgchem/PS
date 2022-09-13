import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
m = max(data)
s = 0
for i in data:
    s += i
print(s / n / m * 100)
