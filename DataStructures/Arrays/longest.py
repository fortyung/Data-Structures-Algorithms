import re

def LongestWord(sen):
    list_of_words = re.findall(r'[a-zA-Z0-9]+', sen) # we used findall instead of split
    # to use split re.split(r'[^a-zA-Z)-9]+', sen) nt:`^`
    sen = max(list_of_words, key=len) # `key=len` will iterate the len func to list_of_word
    # without it in a case of ['boy', 'cat', 'log']
    # it won't return 'boy' has the longest
    # the goal was to to return the longest string, if two characters have the same length return the first element]

    return sen

print(LongestWord('a boy was a cat'))