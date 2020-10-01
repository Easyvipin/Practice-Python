# Read a text file and display the number of vowels/ consonants/
 # uppercase/ lowercase characters present in the file.

vowels ={'a','i','o','e','u'}
with open("dummy.txt","r+") as file:
    lines = file.readlines()
    letters = file.read()

def show_vowels():
    for word in lines:
        for letter in word:
            if letter.lower() in vowels:
                print("Found: " + letter)
def show_consonants():
    for word in lines:
        for letter in word:
            if letter.lower() in vowels:
                print("Found: " + letter)
def show_uppercase():
    count = 0
    for word in lines:
        for letter in word:
            if letter != letter.lower():
                count += 1
    print(f"there are {count} upper letters")
def show_lowercase():
    count = 0
    for word in lines:
        for letter in word:
            if letter == letter.lower():
                count += 1
    print(f"there are {count} lower letters")

show_vowels()