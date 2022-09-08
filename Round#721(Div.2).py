#A
for t in range(int(input())):
    n = int(input())
    c = 0
    while n > 1:
        n = int(n/2)
        c += 1
    print(2**c - 1)

#C
def unorder(list):
    a = []
    b = []
    for i in range(len(list)):
        if list[i] not in a:
            a.append(list[i])
            b.append(1)
        else:
            c = a.index(list[i])
            b[c] += 1
    d = 0
    for i in range(len(b)):
        d += int(b[i]*(b[i]-1)/2)
    return d

for t in range(int(input())):
    n = int(input())
    line = input()
    l = line.split()
    for i in range(n):
        l[i] = int(l[i])
    c = 0
    for i in range(n-1):
        for j in range(i, n):
            c += unorder(l[i:j+1])
    print(c)
