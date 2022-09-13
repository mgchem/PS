import sys
s = sys.stdin.readline().strip()

s = s.upper()
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
m = 0
mv = '?'
for i in d:
    if m < d[i]:
        m = d[i]
        mv = i
    elif m == d[i]:
        mv = '?'
print(mv)
