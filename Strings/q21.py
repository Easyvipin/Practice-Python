#Write a program to find and replace a particular pattern in a string with a given pattern.
#For example:
'''
Enter a sentence: My favourite programming language is Python. This language is very flexible and will not age.
Enter a pattern to find: age
Enter a pattern to replace: xyz
Original Sentence:  My favourite programming language is Python. This language is very flexible and will not age.
Replaced Sentence:  My favourite programming languxyz is Python. This languxyz is very flexible and will not xyz.
'''
#User input
sentence=input("Enter a sentence: ")
pattern=input("Enter a pattern to find: ")
replace=input("Enter a pattern to replace: ")
#pattern length
pLen = len(pattern)
s=sentence2=""
i=0
#replacing the sentence
while i < len(sentence):
    s=sentence[i:pLen+i]
    if s==pattern:
        s=""
        sentence2+=replace
        i+=pLen
    else:
        sentence2+=sentence[i]
        i+=1
print("Original Sentence: ",sentence)
print("Replaced Sentence: ",sentence2)
