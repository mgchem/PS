import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
t = 0
for i in s:
    t += int(i)
print(t)
