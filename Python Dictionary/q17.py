#  Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.

dic = {'1': ['a', 'b'], '2': ['c', 'd']}
valuesList = list(dic.values())

for eachValue1 in valuesList[0]:
    for eachValue2 in valuesList[1]:
        print(eachValue1 + eachValue2)

 # ac ad bc bd
