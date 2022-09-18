import sys
n = int(sys.stdin.readline())
series = 0
num = 665
while series < n:
    num += 1
    if "666" in str(num):
        series += 1
print(num)
