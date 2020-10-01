target = int(input("Enter number to search for: "))

the_list = [1,1,15,15,632,13,2,1,62,3,6,1]

def linear_search(list,target):
    for i in range(len(the_list)):
        if the_list[i] == target:
            return i 
linear_search(the_list,target)