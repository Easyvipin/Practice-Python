# Write a Python program to find the list of words that are longer than n from a given list of words.

totalLength = 5
list = ["vipin", "akashta", "nitin", "subham"]
count = 0
for check in list:
    if len(check) > totalLength:
        count += 1

# 2
