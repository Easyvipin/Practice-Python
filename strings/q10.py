# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. \

print("**** Enter a String *********")

userString = input()
# vipin


# first 2 and last 2 char
# first check its length is not < 2

if len(userString) < 2:
    print("Empty string ")

else:
    print(userString[:2], userString[len(userString)-2:])


# vi in
