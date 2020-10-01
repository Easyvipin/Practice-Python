# Write a Python program to find missing and additional values in two lists. Go to the editor
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h

mainList = ['a', 'b', 'c', 'd', 'g', 'h', 'j']
list1 = ['a', 'b', 'e', 'f']
missingValues = []
addValues = []

for item in list1:
    if item not in mainList:
        missingValues.append(item)
for item in mainList:
    if item not in list1:
        addValues.append(item)

print(missingValues)
print(addValues)
