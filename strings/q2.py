# the following program repeatedly asks users for their age and a password until they provide valid input.
while True:
    print("Enter your age")
    age = input()
    if age.isdecimal():
        break
    print("Enter a valid age (numbers)")

while True:
    print("Enter your Password(letters and numbers only)")
    password = input()
    if password.isalnum():
        print("Age and password is set")
        break
    print("Enter a valid password")


# Enter your age
# 12
# Enter your Password(letters and numbers only)
# 34am
#Age and password is set

""" details 

isdecimal() method returns true when the string contains numbers only.
isalnum() method returns true when the string contains numbers and letters only.
istitle() method return true if string starts with an uppercase letter .
isalpha() method return true if string contain only letters.

"""
