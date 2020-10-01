# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.


def counterString(stringList):
    ctr = 0
    for word in stringList:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr


words = ["vipin", "nitin", "3323", "2342"]
find = counterString(words)
print(find)

# 3
