# Largest Element in the array

def largestelementfn(arr: list) -> int:
    if len(arr) == 1:
        return arr[0]
    else:
        current_largest = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > current_largest:
                current_largest = arr[i]
        return current_largest

arr = [13, 46, 24, 52, 20, 9]
print(largestelementfn(arr))