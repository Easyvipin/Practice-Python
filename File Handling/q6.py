def count(string):
    lower_count = 0
    upper = 0
    for i in string:
        if i == i.lower():
            lower_count+=1
        else:
            upper+=1

    print(f"there are {lower_count} lower case alphabets and {upper} uppercase")