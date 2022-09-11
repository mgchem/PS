import sys

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

n = 1
while n != 0:
    n = int(sys.stdin.readline())
    for i in range(3, n-2, 2):
        if isPrime(i) and isPrime(n-i):
            print("%d = %d + %d" %(n, i, n-i))
            break
