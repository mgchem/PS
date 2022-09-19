import sys
n = int(sys.stdin.readline())
a = n % 5
if a == 0:
    print(n // 5)
elif a == 1:
    print(n // 5 + 1)
elif a == 2:
    if n == 7:
        print(-1)
    else:
        print(n // 5 + 2)
elif a == 3:
    print(n // 5 + 1)
else:
    if n == 4:
        print(-1)
    else:
        print(n // 5 + 2)
