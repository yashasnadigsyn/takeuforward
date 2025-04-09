# Selection Sort

def selectionsortfn(arr: list[int], start_index: int = 0):
    n = len(arr)

    if start_index >= n-1:
        return

    min_index = start_index
    for i in range(start_index+1, n):
        if arr[i] < arr[min_index]:
            min_index = i

    if min_index != start_index:
        arr[start_index], arr[min_index] = arr[min_index], arr[start_index]

    selectionsortfn(arr, start_index+1) 


arr = [13, 46, 24, 52, 20, 9]
print("Original Array: ", arr)
selectionsortfn(arr)
print("Sorted Array: ", arr)
