
#Quick Sort

def QuickSort(arr):
    if len(arr)<1:
        return arr 
    else:
        pivot = arr[0]
        less_than_pivot = [i for i in arr[1:] if i<= pivot]
        greater_than_pivot = [j for j in arr[1:] if j>pivot]
        return QuickSort(less_than_pivot) + [pivot] + QuickSort(greater_than_pivot)
        
print(QuickSort([23,34,12,35,62, 1]))