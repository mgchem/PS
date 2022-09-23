import sys
a, b, c = 0, 0, 1
while a != 0 or b != 0 or c != 0:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        break
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print('right')
    else:
        print('wrong')
