import sys
n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().strip()
    score = 0
    combo = 0
    for ox in s:
        if ox == "O":
            combo += 1
            score += combo
        else:
            combo = 0
    print(score)
