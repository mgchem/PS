import sys

def BiSearch(l, a, s, e):
    if s > e:
        return 0
    m = (s + e) // 2
    if l[m] == a:
        return 1
    elif l[m] > a:
        return BiSearch(l, a, s, m-1)
    else:
        return BiSearch(l, a, m+1, e)

n = int(sys.stdin.readline())
ln = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
lm = list(map(int, sys.stdin.readline().split()))

for i in lm:
    print(BiSearch(ln, i, 0, n-1))
