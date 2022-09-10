import sys
import math
n, k = map(int, sys.stdin.readline().split())

if n >= k:
    print(n-k)
else:
    l = [0]*k
    print(l)
