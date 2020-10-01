def unique(a_list):
    new_list = []
    for i in a_list:
        if i not in new_list:
            new_list.append(i)

    return new_list

my_list = [1,12,41,1,5,15,156,156,153,1,135,9]
print(unique(my_list))
