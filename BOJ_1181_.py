#TLE
import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(sys.stdin.readline().strip())
data = list(set(data))
n = len(data)
for i in range(n-1):
    for j in range(i+1, n):
        if len(data[i]) > len(data[j]):
            data[i], data[j] = data[j], data[i]
        elif len(data[i]) == len(data[j]):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
for w in data:
    print(w)
