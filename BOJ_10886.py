import sys
n = int(sys.stdin.readline())
SurveyCount = 0
AddCount = 0
while AddCount < n and SurveyCount <= n // 2:
    AddCount += 1
    SurveyCount += int(sys.stdin.readline())
if AddCount == n and SurveyCount <= n // 2:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
