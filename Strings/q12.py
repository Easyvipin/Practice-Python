""" Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz' """

string1 = 'abc'
string2 = 'xyz'

char = string1[0] + string1[1]
string1 = string1.replace(char, string2[0] + string2[1])
print(string1)
string2 = string2.replace(string2[0] + string2[1], char)
print(string2)
fullString = string1 + " " + string2
print(fullString)
