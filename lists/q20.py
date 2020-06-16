# Write a Python program to print a list of space-separated elements.

list1 = ["vipin", "john doe", "india", "123 street"]
sepList = []

for item in list1:
    if " " in item:
        sepList.append(item)

print(sepList)
