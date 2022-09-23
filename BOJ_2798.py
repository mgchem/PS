#Brute force

import sys

n, m = map(int, sys.stdin.readline().split())
d = m
data = list(map(int, sys.stdin.readline().split()))
for i in data:
    if m <= i:
        data.remove(i)
for i in range(len(data)-2):
    for j in range(i+1, len(data)-1):
        for k in range(j+1, len(data)):
            if 0 <= m - (data[i] + data[j] + data[k]) < d:
                d = m - (data[i] + data[j] + data[k])
print(m-d)
