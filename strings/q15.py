# Write a Python function that takes a list of words and returns the length of the longest one
listWords = ["vipin", "akash", "abhishek", "john doel"]


def longestLength(listWords):
    length = 0
    for i in listWords:
        if length < len(i):
            length = len(i)
    return length


value = longestLength(listWords)
print(value)
