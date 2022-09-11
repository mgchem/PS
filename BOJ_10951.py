import sys
while 1:
    l = list(map(int, sys.stdin.readline().split()))
    if l == []:
        break
    else:
        print(l[0] + l[1])
