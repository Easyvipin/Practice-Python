import os

print("""\t\tWelcome to Docker Tools
\t\t------------------------""")
while True:

    print("""Press 1 : Image Commands
Press 2 : Container Commands
press 3 : Make a Container for web server
Press 0 : Exit""")

    choice = int(input("Enter your Choice: "))
    while True:
        if choice == 1:
            os.system("clear")
            print("""\t    Press 1: List available Images
            Press 2: Pull New image from the Repo
            Press 3: Remove an image
            Press 0: Go back to Main Menu""")

            choice1 = int(input("Enter your Choice: "))
            if choice1 == 1:
                os.system("docker images")
            elif choice1 == 2:
                repoimg = input("Enter the image you want to download: ")
                os.system("docker pull {}".format(repoimg))
            elif choice1 ==3:
                os.system("docker image ls")
                rmimg = input("Enter the name of the image you want to remove: ")
                os.system("docker image rm {}".format(rmimg))
            elif choice1 == 0:
                break
            else:
                print("INVALID OPTION SELECTED")

        elif choice ==2:
            print("""\t    Press 1: List available Containers
            Press 2: Make a new Container
            Press 3: Remove a Container
            Press 0 : Go back to Main Menu """)

            choice2 = int(input("Enter your Choice: "))
            if choice2 ==1:
                os.system("docker ps -a")
            elif choice2 ==2:
                os.system("docker image ls")
                imgname = input("Enter the name of the OS: ")
                osname = input("Enter the name for your Container: ")
                os.system("docker run -itd --name {} {}".format(osname,imgname))
                print("""\t\tPress 1 to go inside the Conatiner 
                Press 2 to go to previos menu""")
                choice2a = int(input("Enter Your Choice : "))
                if choice2a == 1:
                    os.system("docker attach {}".format(osname))
                elif choice2a == 0:
                    break

            elif choice2 ==3:
                os.system("docker ps -a")
                osname = input("Enter the name of the container to remove permanently: ")
                os.system("docker container rm -f {}".format(osname))
            elif choice2 == 0:
                break
            else:
                print("INVALID OPTION SELECTED")
        elif choice == 3:
            os.system("docker pull web:v1")
            os.system("docker run -itd web:v1")
            print("Server started successfully")
            input("Press ENTER KEY to continue")
            break
        elif choice == 0 :
            exit()
        else:
            print("INVALID OPTION SELECTED")
            break
        
        input("Press ENTER KEY to Continue")
