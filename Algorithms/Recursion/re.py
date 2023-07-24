# counter = 0


def functio(counter):
    if counter > 10:
        return "done"

    check = counter + 1
    print(counter)
    return functio(check)


print(functio(1))
