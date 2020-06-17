# create a birth database system
birthDatabase = {"vipin": 'November 26',
                 "mohit": 'July 13', 'akash': 'August 20'}


while True:
    print("Enter your name ****___****** ")
    yourName = input()
    if yourName == "  ":
        break
    if yourName in birthDatabase:
        print(f"{yourName} Birthday is on {birthDatabase[yourName]}")
    else:
        print("Name does't exists")
        print("Add a birth month and date to add a new data ::")
        birthday = input()
        if birthday == " ":
            print("invalid details")
            break
        birthDatabase[yourName] = birthday
        print("New data added successfully ****************")
