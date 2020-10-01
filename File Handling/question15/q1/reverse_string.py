def reverse_string(string):
    output = ""
    for i in range(len(string)-1,-1,-1):
        output += string[i]
    return output


to_be_reversed = "Jivansh"
answer = reverse_string(to_be_reversed)
print(answer)