# Second Largest Element in the array without Sorting

def secondlargestfn(arr: list) -> int:
    current_largest = arr[0]
    current_second_largest = -1

    if len(arr) == 1: return None
    else:
        for i in range(len(arr)):
            print(current_largest, current_second_largest)
            if arr[i] > current_largest:
                current_second_largest = current_largest
                current_largest = arr[i]
            elif arr[i] > current_second_largest and arr[i] != current_largest:
                current_second_largest = arr[i]
                
        return current_second_largest

arr = [1, 2, 4, 4, 7, 7, 5, 5]
print(secondlargestfn(arr))