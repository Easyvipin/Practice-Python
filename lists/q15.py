# Write a Python program to change the position of every n-th value with the (n+1)th in a list
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]


list1 = [6, 1, 2, 3, 4, 5]
totalLength = len(list1) - 1

for i in range(0, len(list1), 2):
    item = list1[i]
    indexItem = list1.index(item)
    if indexItem < totalLength:
        prevItem = list1[indexItem]
        nextItem = list1[indexItem + 1]
        list1[indexItem + 1] = prevItem
        list1[indexItem] = nextItem

print(list1)


#[1, 2, 3, 4, 5, 6]
