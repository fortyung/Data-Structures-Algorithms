numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 6]


def bubbleSort(array):
    for i in range(1, len(array)):
        for l in range(len(array)):
            if array[l] > array[i]:
                temp = array[i]
                array[i] = array[l]
                array[l] = temp


bubbleSort(numbers)
print(numbers)
