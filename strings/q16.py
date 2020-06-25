# Write a Python program to remove the nth index character from a nonempty string.


def removeChar(givenString, pos):
    newString = ""
    if givenString == "":
        print("empty string")
    else:
        list1 = list(givenString)
        for i in range(len(list1)):
            if pos == i:
                del list1[i]
        for char in list1:
            print(char)
            newString += char
    return newString


value = removeChar("vipin", 2)
print(value)

#viin