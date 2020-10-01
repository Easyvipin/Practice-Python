import os
import getpass
os.system("tput setaf 2")
    
print("""\t\t\tWelcome To My TUI which makes work easy
\t\t\t----------------------------------------""")

os.system("tput setaf 7")

while True:
    pwd = getpass.getpass("enter your password: ")
    crct_pwd = "root"
    if pwd != crct_pwd:
        print("Incorrect password,Try again")
        continue
    else:
        break
 

location = input("Where do you want to run your Program (local/remote)")

if location == "remote":
    print(location)
    remote_ip = input("Enter host IP: ")
    os.system("ssh-copy-id root@{}".format(remote_ip ))
elif location == "local":
    print(location)
else:
    print("option not valid")
    quit()


while True:
    input("Press Enter to Continue")    #to make the input stay on screen
    os.system("clear")
    print("""press 1 to see date
press 2 to see calendar
press 3 to create web server
Press 4 to give a Custom command
Press 7 : to exit""")
    
    x=int(input("enter your choice: "))
    if location == "local":
        if x==1:
            os.system("date")
        elif x==2:
            os.system("cal")
        elif x==3:
            os.system("systemctl start httpd")
            print("Go to http://10.0.2.15 to access the server")
        elif x==4:
            cmd = input("Enter your Command : ")
            os.system("{}".format(cmd))    
        elif x==7:
            exit()
        else:
            print("Invalid Option")        
    else:

        if x==1:
            os.system("ssh {} date".format(remote_ip))
        elif x==2:
            os.system("ssh {} cal".format(remote_ip))
        elif x==4:
            cmd= input("Enter your Command : ")
            os.system("ssh {} {}".format(remote_ip,cmd))
        elif x==7:
            exit()
        else:
            print("Invalid Option")
