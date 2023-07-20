def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    return True if len(nums) > len(set(nums)) else False

print(containsDuplicate([1,2,2,4]))