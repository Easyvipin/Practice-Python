"""  Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters """


def changeUppercase(givenString):
    num_counter = 0
    for letter in givenString[:4]:
        if letter.upper() == letter:
            num_counter += 1
        if num_counter >= 2:
            return givenString.upper()
    return givenString


value = changeUppercase("viPIn")
print(value)

#VIPIN