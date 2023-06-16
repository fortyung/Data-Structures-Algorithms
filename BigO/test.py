

def containsPairSum(arr, sum):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j]) == sum:
                return True
    return False

lop = [1,4,3,6]


# print(containsPairSum(lop, 8))

# def compare_pairs(arr, num):
#     seen = set()
#     for element in arr:
#         complement = num - element
#         print(complement)
        
#         if complement in seen:
#             return True
#         seen.add(element)
#         print(seen)
#     return False

# print(compare_pairs(lop, 8))

def compare_pairs(arr, sum):
    my_set = set()
    for nums in arr:
        if (sum - nums) in my_set:
            return True
        my_set.add(nums)
    return False

print(compare_pairs(lop, 8))
