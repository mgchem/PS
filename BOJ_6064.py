import sys
import math
T = int(sys.stdin.readline())

def lcm(a, b):
    return a * b // math.gcd(a, b)

for t in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    if 1 <= x <= M and 1 <= y <= N:
        if x == y:
            print(x)
        elif x < y:
            sub = y - x
            b = 0
            for i in range(lcm(M, N) // N):
                if (N * i + sub) % M == 0:
                    b = 1
                    print(N * i + y)
            if b == 0:
                print(-1)
        else:
            sub = x - y
            b = 0
            for i in range(lcm(M, N) // M):
                if (M * i + sub) % N == 0:
                    b = 1
                    print(M * i + x)
            if b == 0:
                print(-1)
    else:
        print(-1)
