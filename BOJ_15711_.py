#TLE

import sys
T = int(sys.stdin.readline())

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    if A + B == 2 or A + B == 3:
        print("NO")
    elif (A + B) % 2 == 0:
        print("YES")
    else:
        if isPrime(A+B - 2):
            print("YES")
        else:
            print("NO")
