#Queue

import sys

n = int(sys.stdin.readline())

def main(n):
    queue = []
    for i in range(n):
        s = sys.stdin.readline().strip()
        if "push" in s:
            queue.append(int(s[5::]))
        elif "pop" in s:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
                queue = queue[1::]
        elif "size" in s:
            print(len(queue))
        elif "empty" in s:
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif "front" in s:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        else:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])

main(n)
