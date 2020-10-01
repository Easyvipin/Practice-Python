# . Write a Python program to convert a list of characters into a string.


def makeString(givenList):
    newWord = ""
    return newWord.join(givenList)


# joins is method takes all item in iterable and joins them in one string
charList = ['v', 'i', 'p', 'i', 'n']
newString = makeString(charList)
print(newString)

# vipin
