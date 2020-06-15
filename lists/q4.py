# Write a Python program to get the smallest number from a list.


def smallerNo(numberList):
    min = numberList[0]
    for eachNo in numberList:
        if eachNo < min:
            min = eachNo
    return min


number = [110.1, 110.2, 2, 3, 4, 5]
smallestNo = smallerNo(number)
print(smallestNo)
