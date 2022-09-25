#Double ended queue

import sys

n = int(sys.stdin.readline())

def main(n):
    deque = []
    for i in range(n):
        s = sys.stdin.readline().strip()
        if "push_front" in s:
            deque = [int(s[11::])] + deque
        elif "push_back" in s:
            deque.append(int(s[10::]))
        elif "pop_front" in s:
            if len(deque) == 0:
                print(-1)
            else:
                print(deque[0])
                deque = deque[1::]
        elif "pop_back" in s:
            if len(deque) == 0:
                print(-1)
            else:
                print(deque[-1])
                deque = deque[:-1:]
        elif "size" in s:
            print(len(deque))
        elif "empty" in s:
            if len(deque) == 0:
                print(1)
            else:
                print(0)
        elif "front" in s:
            if len(deque) == 0:
                print(-1)
            else:
                print(deque[0])
        else:
            if len(deque) == 0:
                print(-1)
            else:
                print(deque[-1])

main(n)
