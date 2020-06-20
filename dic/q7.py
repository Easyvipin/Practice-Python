# Write a Python script to sort (ascending and descending) a dictionary by value.

spam = {'rahul': 23, 'vipin': 21, 'prince': 25, 'kas': 17}
valueList = list(spam.items())
valueList.sort()
sortedSpam = dict(valueList)
print(sortedSpam)
