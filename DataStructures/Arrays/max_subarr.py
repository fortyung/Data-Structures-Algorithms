def max_subarray_sum(nums):
    current_max = nums[0]
    global_max = nums[0]
    
    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        global_max = max(global_max, current_max)
    
    return global_max

nums = [5]
max_sum = max_subarray_sum(nums)
print(max_sum)