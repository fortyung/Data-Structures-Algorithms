"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = set()


        for i in range(len(nums)):
            counterpart = target - nums[i]

            if counterpart in  seen:
                index1 = nums.index(counterpart)
                index2 = i

                return [index1, index2]

            seen.add(nums[i])

        return []

obj = Solution()
print(obj.twoSum([1,3,2,3], 7))
