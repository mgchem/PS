#A
t = int(input())
nList = []
sList = []
for i in range(t):
    nList.append(int(input()))
    sList.append(input().strip())
for i in range(len(nList)):
    if nList[i] != 5:
        print("NO")
    else:
        if "T" in sList[i] and "i" in sList[i] and "m" in sList[i] and "u" in sList[i] and "r" in sList[i]:
            print("YES")
        else:
            print("NO")


#B
t = int(input())
nList = []
r1List = []
r2List = []
for i in range(t):
    nList.append(int(input()))
    r1List.append(input().strip())
    r2List.append(input().strip())
for i in range(len(nList)):
    b = 0
    for j in range(nList[i]):
        if r1List[i][j] == "R" or r2List[i][j] == "R":
            if r2List[i][j] != r1List[i][j]:
                b = 1
    if b == 1:
        print("No")
    else:
        print("YES")

#C #TLE!!
t = int(input())
for i in range(t):
    n = int(input())
    s1, s2, s3 = 0, 0, 0
    p1List = input().split()
    p2List = input().split()
    p3List = input().split()
    j = 0
    while j < n:
        k = p1List[j]
        if k in p2List and k in p3List:
            del p1List[j]
            p2List.remove(k)
            p3List.remove(k)
            n -= 1
        elif k in p2List:
            s1 += 1
            s2 += 1
            del p1List[j]
            p2List.remove(k)
            n -= 1
        elif k in p3List:
            s1 += 1
            s3 += 1
            del p1List[j]
            p3List.remove(k)
            n -= 1
        else:
            j += 1
    j = 0
    n = len(p2List)
    while j < n:
        k = p2List[j]
        if k in p3List:
            s2 += 1
            s3 += 1
            del p2List[j]
            p3List.remove(k)
            n -= 1
        else:
            j += 1
    s1 += len(p1List)*3
    s2 += len(p2List)*3
    s3 += len(p3List)*3
    print(s1, s2, s3)
