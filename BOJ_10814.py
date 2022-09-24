#Quick sort

import sys

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
data = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    data.append([age, name, i])

def qsort(arr):
    def sort(l, r):
        if r <= l:
            return
        m = partition(l, r)
        sort(l, m - 1)
        sort(m, r)
    
    def partition(l, r):
        p1 = arr[(l + r) // 2][0]
        p2 = arr[(l + r) // 2][2]
        while l <= r:
            while arr[l][0] < p1 or arr[l][0] == p1 and arr[l][2] < p2:
                l += 1
            while arr[r][0] > p1 or arr[r][0] == p1 and arr[r][2] > p2:
                r -= 1
            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l + 1, r - 1
        return l
    
    sort(0, len(arr) - 1)
    return arr

data = qsort(data)
for i in data:
    print(i[0], i[1])
