# Write a Python function to reverses a string if it's length is a multiple of 4.


def reverseString(givenString):
    newString = ""
    if len(givenString) % 4 == 0:
        print("hello")
        for i in range(len(givenString)-1, -1, -1):
            newString += givenString[i]
    return newString


value = reverseString("vipi")
print(value)

# ipiv
