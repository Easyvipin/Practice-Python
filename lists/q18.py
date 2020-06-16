# Write a Python program to generate groups of five consecutive numbers in a list.

list1 = [1, 2, 3, 4, 5, 7, 6, 9, 10]
consList = []

for item in list1:
    indexItem = list1.index(item)
    if item + 1 == list1[indexItem+1]:
        consList.append(item)
    else:
        consList.append(item)
        break
print(consList)
#[1, 2, 3, 4, 5]
