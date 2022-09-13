import sys
T = int(sys.stdin.readline())
for i in range(T):
    R, S = sys.stdin.readline().split()
    R = int(R)
    s = ""
    for i in S:
        s += i*R
    print(s)
