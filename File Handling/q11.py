with open("dummy.txt","r+") as file:
    read = file.readlines()
    for i in read:
        print("#" + i)