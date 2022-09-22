import sys

n = int(sys.stdin.readline())

b = 0
for i in range(1, n):
    istr = str(i)
    tot = i
    for num in istr:
        tot += int(num)
    if tot == n:
        b = 1
        print(i)
        break
if b == 0:
    print(0)
