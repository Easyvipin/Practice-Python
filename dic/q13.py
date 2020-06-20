# Write a Python program to get the maximum and minimum value in a dictionary.

spam = {'rahul': 25, 'vipin': 21, 'prince': 29, 'kas': 17}
allValues = list(spam.values())
maxvalue = allValues[0]
for value in allValues:
    if maxvalue < value:
        maxvalue = value

print(maxvalue)
