# Insertion Sort

def insertionsortfn(arr: list[int]):
    for i in range(0, len(arr), 1):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1


arr = [13, 46, 24, 52, 20, 9]
print("Before Sorting: ", arr)
insertionsortfn(arr)
print("After Sorting: ", arr)
