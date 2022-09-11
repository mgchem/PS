import sys
T = int(sys.stdin.readline())
ModList = [[10], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a %= 10
    print(ModList[a][b%len(ModList[a])])
