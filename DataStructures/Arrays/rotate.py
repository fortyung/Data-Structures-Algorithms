def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # new_list = nums[0:k]
        # del nums[0:k]

        # nums.extend(new_list)

        # return nums

        k = k % len(nums)  # Adjust k if it's greater than the length of the list

        new_list = nums[-k:]  # Get the last k elements of nums
        del nums[-k:]  # Delete the last k elements from nums

        nums[:0] = new_list  # Insert new_list at the beginning of nums



print(rotate([1,2,3,8,4,5,6], 1))