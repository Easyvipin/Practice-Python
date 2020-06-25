# Write a Python program to get the last part of a string before a specified character.


def getLastPart(givenString, char):
    pos = givenString.find(char)
    return givenString[pos+1:]


value = getLastPart("the strongest man is called-teminator", "-")
print(value)

# teminator
