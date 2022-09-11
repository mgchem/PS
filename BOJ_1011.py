import sys
T = int(sys.stdin.readline())
for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    d = y - x
    if d == 1 or d == 2 or d == 3:
        print(d)
    else:
        n = 2
        while n ** 2 < d:
            n += 1
        if n ** 2 == d:
            print(2 * n - 1)
        else:
            d -= (n-1) ** 2
            cnt = 0
            k = n-1
            while k > 0 and d > 0:
                cnt += d // k
                d %= k
                k -= 1
            print(2 * n - 3 + cnt)
