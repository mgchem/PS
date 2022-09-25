#Quick sort

import sys

n = int(sys.stdin.readline())
data = []

def merge_sort(arr):
    def sort(l, r):
        if r - l < 2:
            return
        m = (l + r) // 2
        sort(l, m)
        sort(m, r)
        merge(l, m ,r)
    
    def merge(l, m, r):
        tl = []
        low, high = l, m
        
        while low < m and high < r:
            if arr[low][0] < arr[high][0]:
                tl.append(arr[low])
                low += 1
            elif arr[low][0] == arr[high][0]:
                if arr[low][1] < arr[high][1]:
                    tl.append(arr[low])
                    low += 1
                else:
                    tl.append(arr[high])
                    high += 1
            else:
                tl.append(arr[high])
                high += 1
        while low < m:
            tl.append(arr[low])
            low += 1
        while high < r:
            tl.append(arr[high])
            high += 1
        
        for i in range(l, r):
            arr[i] = tl[i - l]
    
    sort(0, len(arr))
    return arr

for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
for i in merge_sort(data):
    print(str(i[0]) + " " + str(i[1]))
