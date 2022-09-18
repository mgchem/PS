import sys
n = int(sys.stdin.readline())
while n != 0:
    strn = str(n)
    strnrev = strn[::-1]
    if strn == strnrev:
        print("yes")
    else:
        print("no")
    n = int(sys.stdin.readline())
