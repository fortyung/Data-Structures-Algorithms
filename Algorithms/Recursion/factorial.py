def findFactorialRecursive(number):  # O(n)
    nextNumber = number - 1

    if number <= 1:
        return number

    return number * findFactorialRecursive(nextNumber)


def findFactorialIterative(number):  # O(n)
    num = 1
    if number == 0:
        return 0

    for i in range(1, number + 1):
        num = num * i

    return num


print(findFactorialRecursive(0))

# print(findFactorialIterative(1))
