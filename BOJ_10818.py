import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
mi = data[0]
ma = data[0]
for i in data:
    if mi > i:
        mi = i
    if ma < i:
        ma = i
print(mi, ma)
