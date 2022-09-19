import sys

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
cnt = 0
for num in data:
    if isPrime(num):
        cnt += 1
print(cnt)
