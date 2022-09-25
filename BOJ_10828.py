#Stack

import sys

n = int(sys.stdin.readline())

def main(n):
    stack = []
    for i in range(n):
        s = sys.stdin.readline().strip()
        if "push" in s:
            stack.append(int(s[5::]))
        elif "pop" in s:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
                stack = stack[:-1:]
        elif "size" in s:
            print(len(stack))
        elif "empty" in s:
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        else:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])

main(n)
