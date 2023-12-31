test_list1 = [1, 6, 8, 7]
test_list2 = [4, 6, 3, 0]
# using naive method
# to combine two sorted lists

size_1 = len(test_list1)
size_2 = len(test_list2)

res = []
i, j = 0, 0

while i < size_1 and j < size_2:
    if test_list1[i] < test_list2[j]:
        res.append(test_list1[i])
        i += 1

    else:
        res.append(test_list2[j])
        j += 1

res = res + test_list1[i:] + test_list2[j:]

# printing result
print("The combined sorted list is : " + str(res))
