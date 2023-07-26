def reverseStringIterative(wod):
    # return word[::-1]

    word = list(wod)
    for i in range(len(word) // 2):
        temp = word[i]
        word[i] = word[len(word) - 1 - i]
        word[len(word) - 1 - i] = temp

    return "".join(word)


def reverseRecursive(strr):
    size = len(strr)

    if size == 0:
        return

    last_char = strr[size - 1]

    print(last_char, end="")
    reverseRecursive(strr[0 : size - 1])


reverseRecursive("young")
