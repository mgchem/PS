import sys
data = []
for i in range(9):
    data.append(int(sys.stdin.readline()))
m = 0
idx = 0
for i in range(9):
    if m < data[i]:
        m = data[i]
        idx = i+1
print(m)
print(idx)
