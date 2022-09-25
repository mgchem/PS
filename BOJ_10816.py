import sys

n = int(sys.stdin.readline())
datan = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
datam = list(map(int, sys.stdin.readline().split()))
dictn = {}
for i in datan:
    if i in dictn:
        dictn[i] += 1
    else:
        dictn[i] = 1
data = []
for i in datam:
    if i in dictn:
        data.append(dictn[i])
    else:
        data.append(0)
s = ""
for i in data:
    s += str(i)
    s += " "
print(s[:-1:])
