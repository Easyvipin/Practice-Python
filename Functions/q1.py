#Write a function to check if a string is palindrome or not
def palstr (sarg):
    '''takes a string argument'''
    if len(sarg) % 2 == 0:
        mid = int(len(sarg)/2)
    else:
        mid = int(len(sarg)/2 + 1)
    flag = 0
    for i in range (0, mid):
        if  sarg [i] != sarg[len(sarg)-1-i] :
            flag = 0
            break
        else:
            flag = 1
            
            
    if flag == 0:
        return False
    else:
        return True
inp = input("enter to check")
palstr(inp)
