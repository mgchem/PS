import sys
A, B = map(int, sys.stdin.readline().split())
if A == B:
    print(A)
else:
    if A <= 0 and B <= 0:
        if A < B:
            print(B*(B-1)//2 - A*(A-1)//2 + B)
        else:
            print(A*(A-1)//2 - B*(B-1)//2 + A)
    elif A <= 0 and B >= 0:
        print(B*(B+1)//2 - A*(A-1)//2)
    elif A >= 0 and B <= 0:
        print(A*(A+1)//2 - B*(B-1)//2)
    else:
        if A < B:
            print(B*(B+1)//2 - A*(A-1)//2)
        else:
            print(A*(A+1)//2 - B*(B-1)//2)
