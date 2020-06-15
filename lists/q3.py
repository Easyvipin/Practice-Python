# Write a Python program to get the largest number from a list

# large no function


def largeNo(numberList):
    max = numberList[0]
    for eachNo in numberList:
        if eachNo > max:
            max = eachNo
    return max


number = [110.1, 110.2, 2, 3, 4, 5]
largestNo = largeNo(number)
print(largestNo)

# 110.2
