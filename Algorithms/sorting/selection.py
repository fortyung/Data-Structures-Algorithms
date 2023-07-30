numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 6]


def selectionSort(array):
    for i in range(len(array)):
        min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j

        array[i], array[min] = array[min], array[i]

    return array


print(selectionSort(numbers))
