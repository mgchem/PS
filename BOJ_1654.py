#Binary search

import sys
k, n = map(int, sys.stdin.readline().split())
data = []
tot = 0
for i in range(k):
    data.append(int(sys.stdin.readline().strip()))
    tot += data[-1]

def Bi(l, a, s, e):
    if s > e:
        return s-1
    m = (s + e) // 2
    c = 0
    for num in l:
        c += num // m
    if c >= a:
        return Bi(l, a, m+1, e)
    else:
        return Bi(l, a, s, m-1)

print(Bi(data, n, 1, tot // n))
