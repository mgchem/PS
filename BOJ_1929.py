def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

l = input().split()
n, m = int(l[0]), int(l[1])
for i in range(n, m+1):
    if isPrime(i):
        print(i)
