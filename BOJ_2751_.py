#quick sort

import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline()))

sys.setrecursionlimit(10**6)

def qsort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[len(arr) // 2]
    larr, rarr = [], []
    for num in arr:
        if num < p:
            larr.append(num)
        else:
            rarr.append(num)
    return qsort(larr) + [p] + qsort(rarr)

data = qsort(data)
for i in data:
    print(i)
