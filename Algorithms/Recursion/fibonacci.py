def fibonacciIterative(n):
    if n < 2:
        return n

    first = 0
    sec = 1

    for i in range(1, n):
        fib = first + sec
        first = sec
        sec = fib

    return fib


def fibonacciRecursive(n):
    if n < 2:
        return n

    return fibonacciRecursive(n - 2) + fibonacciRecursive(n - 1)


# print(fibonacciRecursive(4))
print(fibonacciIterative(0))
