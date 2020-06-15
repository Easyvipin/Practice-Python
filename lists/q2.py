# Write a Python program to multiplies all the items in a list.


def findProduct(numberList):
    product = 1
    for count in numberList:
        product *= count
    return product


number = [1, 2, 3, 4, 5]
# CALL
totalProduct = findProduct(number)
print(totalProduct)

#120
