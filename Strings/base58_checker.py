#!bin/Python3

#Question: Create a script which checks the string if it is base58 encoded or not.


#This Program checks if Encoded string is base58 or not.
 
userin = input("Enter your String: ")  #this line will take input from user 
if ('I' not in userin) and ('O' not in userin) and ('l' not in userin) and (len(set(userin)) < 58) and ('0' not in userin):     
  print("The string is Base58") 
else:
  print("the string is not Base58")



#First it checks idiviually for 'I', 'O', 'l' and '0'And then it checks if there are 58 unique charactersWhen u convert a list to a set all duplicate values will be deletedSo a string "aaa" will give:set(string) = {'a'}And length of the set will give u the length of the unique letters
