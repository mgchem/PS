import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

t = 0
m = 0
for i in range(M, N+1):
    if isPrime(i):
        t += i
        if m == 0:
            m = i
if t == 0:
    print(-1)
else:
    print(t)
    print(m)
