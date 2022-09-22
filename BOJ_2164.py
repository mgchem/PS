import sys
import collections

n = int(sys.stdin.readline())
card = collections.deque([])

for i in range(1, n+1):
    card.append(i)
    
while len(card) > 1:
    p = card.popleft()
    card.rotate(-1)

print(card[0])
