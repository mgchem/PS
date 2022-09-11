import sys
N = int(sys.stdin.readline())
AiList = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

cnt = 0
for i in range(N):
    if AiList[i] <= B:
        cnt += 1
    elif (AiList[i] - B) % C == 0:
        cnt += (AiList[i] - B) // C + 1
    else:
        cnt += (AiList[i] - B) // C + 2
print(cnt)
