def check(nums: list, n: int) -> bool:
    for i in range(len(nums)-1):
        if nums[i+1] < nums[i]:
            start_index = i+1
            break

    for i in range(n-1):
        print(nums[start_index], nums[start_index+1])
        if nums[start_index+1] < nums[start_index]:
            return False
        start_index += 1
        
    return True

#nums = [3,4,4,5,5,1,1,2]
# 3 4 5 1 2 3 4 5 1 2
nums = [1,2,3,4]
# nums = [1,2,2,3,3]
n = len(nums)
nums += nums
print(check(nums, n))