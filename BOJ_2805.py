#Binary search

import sys
n, m = map(int, sys.stdin.readline().split())
data = sorted(list(map(int, sys.stdin.readline().split())))

def Bi(l, a, s, e):
    if s > e:
        return s-1
    m = (s + e) // 2
    c = 0
    for num in l:
        if num > m:
            c += num - m
    if c >= a:
        return Bi(l, a, m+1, e)
    else:
        return Bi(l, a, s, m-1)

print(Bi(data, m, 0, data[-1]))
