# Bubble Sort

def bubblesortfn(arr: list[int]):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i, 1):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

    return arr

arr = [13, 46, 24, 52, 20, 9]
print("Original Array: ", arr)
bubblesortfn(arr)
print("Sorted Array: ", arr)
