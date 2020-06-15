# Whats on your luck
print("Type your Lucky no")
yourNumber = int(input())

# function


def checkLuck(yourNumber):
    if yourNumber == 1:
        print("happy person")
    elif yourNumber == 2:
        print("lucky person")
    elif yourNumber == 3:
        print("strong person")
    elif yourNumber == 4:
        print("RESPECTFUL")
    elif yourNumber == 5:
        print("sports person")


if(yourNumber > 0 and yourNumber <= 5):
    checkLuck(yourNumber)
else:
    print("Enter no between 1 and 5")
