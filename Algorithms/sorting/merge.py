numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 5, 0]


def mergeSort(array):
    if len(array) == 1:
        return array

    # index is used to find the middle index.
    index = len(array) // 2

    # Here I split the array into left and right using the index
    left = array[:index]
    right = array[index:]

    # I am merging both left and right on every level of the recursion
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    return result + left[i:] + right[j:]


answer = mergeSort(numbers)
print(answer)
