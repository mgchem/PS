import sys
t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    cnt = 1
    focus = data[m]
    location = [0] * m + [1] + [0] * (n-m-1)
    while location[0] != 1 or data[0] != max(data):
        if data[0] == max(data):
            del data[0]
            del location[0]
            cnt += 1
        else:
            data = data[1:] + [data[0]]
            location = location[1:] + [location[0]]
    print(cnt)
