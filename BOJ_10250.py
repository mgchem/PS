import sys

t = int(sys.stdin.readline())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    m, l = n // h + 1, n % h
    if l == 0:
        l = h
        m -= 1
    sm = str(m)
    if len(sm) == 1:
        sm = "0" + sm
    print(str(l) + sm)
