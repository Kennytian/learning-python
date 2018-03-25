# coding: utf-8
def break_words(stuff):
    words = stuff.split(' ')
    return words


words = break_words('This function will break up words for us')
print(words)


def sort_words(stuff):
    return sorted(stuff)


print(sort_words('Sorts the words.'))


# [' ', ' ', '.', 'S', 'd', 'e', 'h', 'o', 'o', 'r', 'r', 's', 's', 't', 't', 'w']

def getFirstWord(stuff):
    word = stuff.pop(0)
    return word


print(getFirstWord(words))  # This


def getLastWord(stuff):
    word = stuff.pop(-1)
    return word


print(getLastWord(words))  # us


