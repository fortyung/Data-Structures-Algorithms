numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 6]


def insertSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            print(array)
        array[j + 1] = key
        print(array)


insertSort(numbers)
# print(numbers)
