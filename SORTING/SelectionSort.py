
# Selection sort

arr = [23,53,12,63,73]

def selectionSorting(arr):
    n = len(arr)
    for i in range(n-1):
        mi = i
        for j in range(i+1, n):
            if (arr[mi]>arr[j]):
                mi = j
        temp = arr[mi]
        arr[mi] = arr[j]
        arr[j] = temp
    return arr

print(selectionSorting(arr))