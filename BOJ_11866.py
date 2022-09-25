import sys

n, k = map(int, sys.stdin.readline().split())
data = []
dataa = []
for i in range(n):
    data.append(i+1)
idx = -1
while len(data) > 1:
    idx = (idx + k) % len(data)
    dataa.append(data[idx])
    data.remove(data[idx])
    idx -= 1
dataa.append(data[0])
s = "<"
for i in dataa:
    s += str(i) + ", "
print(s[:-2:] + ">")
