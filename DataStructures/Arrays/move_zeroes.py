def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    l = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[l]
            nums[l] = nums[i]
            nums[i] = temp

            l += 1
    return nums

print(moveZeroes([10,0,5,0,0]))
