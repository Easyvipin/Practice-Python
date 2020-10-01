with open("dummy.txt","r+") as file:
    lines = file.readlines()
    freq = {} 
    for i in lines:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1


    vals = freq.values()
    Keys = freq.keys()
    max_val = 0  
    max_idx = 0
    for i in range(len(vals)):
        if vals[i] > max_val:
            max_val = vals[i] 
            max_idx = i
    max_key = Keys[max_idx]
    print("The most common word is " + max_key)





