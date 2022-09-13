import sys
s = set()
for i in range(10):
    a = int(sys.stdin.readline())
    s.add(a%42)
print(len(s))
