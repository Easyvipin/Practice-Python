# Write a Python program to count the number of characters (character frequency) in a string.
randomString = "google.com"
list1 = list(randomString)
count = 0
frequencyDic = {}
for i in list1:
    if i in frequencyDic:
        frequencyDic[i] = frequencyDic[i] + 1
    else:
        frequencyDic[i] = 1
print(frequencyDic)

#{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
