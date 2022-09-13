import sys
data = [0]*10
s = 1
for i in range(3):
    s *= int(sys.stdin.readline())
s = str(s)
for i in s:
    data[int(i)] += 1
for i in data:
    print(i)
