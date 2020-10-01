# With a given tuple (1,2,3,4,5,6,7,8,9,10), define a function to print the first half values
# in one line and the second half values in another line.

tup = (1,2,3,4,5,6,7,8,9,10)
def seperate(tup):
    mid = len(tup)//2
    for i in range(mid):
        print(tup[i], end=' ')
    print()
    for j in range(mid,len(tup)):
        print(tup[j], end=' ')


seperate(tup)