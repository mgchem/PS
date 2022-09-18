#stack

import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline()))
stack = []
direction = []
for num in range(1, n+1):
    stack.append(num) #push
    direction.append("+")
    while len(stack) != 0 and len(data) != 0 and stack[-1] == data[0]:
        del stack[-1] #pop
        del data[0]
        direction.append("-")
if len(data) != 0 or len(stack) != 0:
    print("NO")
else:
    for d in direction:
        print(d)
