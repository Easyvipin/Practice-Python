target = int(input("Enter number to search for: "))

the_list = [1,2,3,4,5,6,7,8,9]

low = 0
high = len(the_list)
def binary_search(the_list,target,low,high):
    mid = (low + high)//2 + low
    if(the_list[mid] == target):
        return mid
    if the_list[mid] > target:
        return binary_search(the_list,target,low,mid-1)
    else:
        return binary_search(the_list,target,mid+1,high)

answer = binary_search(the_list,target,low,high)
print(answer)