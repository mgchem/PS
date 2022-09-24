import sys

n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().strip()
    c = 1
    while len(s) > 1 and c != 0:
        c = 0
        if "()" in s:
            s = s.replace("()", "")
            c = 1
    if len(s) != 0:
        print("NO")
    else:
        print("YES")
