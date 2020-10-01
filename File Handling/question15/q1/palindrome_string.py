def reverse_string(string):
    output = ""
    for i in range(len(string)-1,-1,-1):
        output += string[i]
    return output

def check_palindrome(string):
    reversed_version = reverse_string(string)
    if string == reversed_version:
        print("Palindrome")
        return
    else:
        print("Nope")
        return



check_palindrome("lalal")