# Write a Python program to remove duplicates from a list.


def removeDuplicates(givenList):
    for item in givenList:
        count = 0
        for item2 in givenList:
            if item == item2:
                count += 1
                if count >= 2:
                    givenList.remove(item2)
    return givenList


nameList = ["vipin", "nitin", "vipin", "akash", "nitin"]

removeDuplicates(nameList)
print(nameList)

# ['vipin', 'akash', 'nitin']