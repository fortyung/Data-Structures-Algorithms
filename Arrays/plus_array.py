def mergeSortedArrays(array1, array2):
    new_arr = []
    count = 0

    if len(array1) == 0:
        return array2
    if len(array2) == 0:
        return array1
    
    for i in range(min(len(array1), len(array2))):
        if array1[i] <= array2[i]:
            new_arr.append(array1[i]) 
            new_arr.append(array2[i])
        else:
            new_arr.append(array2[i])
            new_arr.append(array1[i])
        count +=1

    if len(array2) > len(array1):
        new_arr.extend(array2[count:])
    elif len(array2) < len(array1):
        new_arr.extend(array1[count:])

    return new_arr


print(mergeSortedArrays([1,3], []))
