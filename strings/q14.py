""" Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!' """

string = 'The lyrics is not that poor!'
notPost = string.find("not")
poorPost = string.find('poor')

if poorPost > notPost and notPost > 0 and poorPost > 0:
    string = string.replace(string[notPost:poorPost+4], "good")

print(string)
