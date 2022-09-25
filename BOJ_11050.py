import sys

n, k = map(int, sys.stdin.readline().split())
ans = 1
if k == 0 or k == n:
    print(ans)
else:
    if n // 2 >= k:
        for i in range(n-k+1, n+1):
            ans *= i
        sub = 1
        for i in range(1, k+1):
            sub *= i
        ans = ans // sub
    else:
        for i in range(k+1, n+1):
            ans *= i
        sub = 1
        for i in range(1, n-k+1):
            sub *= i
        ans = ans // sub
    print(ans)
