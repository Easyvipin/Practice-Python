# Write a Python program to sum all the items in a list.
def findSum(numberList):
    sum = 0
    for count in numberList:
        sum += count
    return sum


number = [1, 2, 3, 4, 5]
# CALL
totalSum = findSum(number)
print(totalSum)

# 15
