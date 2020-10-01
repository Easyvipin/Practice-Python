# Write a Python function that takes two lists and returns True if they have at least one common member.

list1 = ["vipin", "nitin", "akash", "john"]
list2 = ["lorem", "ipsum", "john", "nitin"]

# function


def checkCommon(list1, list2):
    for check in list1:
        if check in list2:
            return True
            break
    return False


istrue = checkCommon(list1, list2)

# True
