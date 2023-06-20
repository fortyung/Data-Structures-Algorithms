# def reverse_array(wod):
#     for i  in range(len(wod) // 2):
#         temp = wod[i]
#         wod[i] = wod[len(wod) - 1 - i]
#         wod[len(wod) - 1 - i] = temp
#     print(wod)

# reverse_array('lopp')

# def reverse_string(strr):
#     if type(strr) != str or len(strr) < 2:
#         raise Exception('Invalid input')
    
#     word = list(strr)
#     word_length = len(strr) - 1

#     for i  in range(len(word) // 2):
#         temp = word[i]
#         word[i] = word[word_length - i]
#         word[word_length - i] = temp

#     new_word = ''.join(word)
#     return new_word

# print(reverse_string('123'))


def reverse2(strr):
    if type(strr) != str or len(strr) < 2:
        raise Exception('Invalid input')
    
    word = strr[::-1]
    return word

reverse2('young')
