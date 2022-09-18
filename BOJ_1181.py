#Quick sort

import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(sys.stdin.readline().strip())
data = list(set(data))

def qsort(arr):
    def sort(low, high):
        if high <= low:
            return
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)
    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while len(arr[low]) < len(pivot) or (len(arr[low]) == len(pivot) and arr[low] < pivot):
                low += 1
            while len(arr[high]) > len(pivot) or (len(arr[high]) == len(pivot) and arr[high] > pivot):
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low
    sort(0, len(arr) - 1)
    return arr

for w in qsort(data):
    print(w)
