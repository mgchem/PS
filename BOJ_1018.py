import sys
n, m = map(int, sys.stdin.readline().split())
data = []

set1 = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
set2 = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]

for i in range(n):
    data.append(sys.stdin.readline().strip())
minChange = 64
for y in range(n-7):
    for x in range(m-7):
        numChange1 = 0
        numChange2 = 0
        for i in range(8):
            for j in range(8):
                if data[y+i][x+j] != set1[i][j]:
                    numChange1 += 1
                else:
                    numChange2 += 1
        minChange = min(minChange, numChange1, numChange2)
print(minChange)
