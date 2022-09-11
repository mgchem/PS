import sys
A, B, C = map(int, sys.stdin.readline().split())

def Pow(a, b, c):
    if b == 1:
        return a % c
    elif b == 2:
        return (a * a) % c
    elif b % 2 == 0:
        return (Pow(a, b // 2, c) ** 2) % c
    else:
        return (Pow(a, b // 2, c) ** 2 * a) % c

print(Pow(A, B, C))
