l = input().split()
a, b, v = int(l[0]), int(l[1]), int(l[2])
if v>a:
    if (v-a)%(a-b) == 0:
        print(int((v-a)/(a-b)+1))
    else:
        print(int((v-a)/(a-b)+2))
else:
    print(1)
