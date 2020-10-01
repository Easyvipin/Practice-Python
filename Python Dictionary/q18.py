# Write a Python program to find the highest 3 values in a dictionary

d1 = {'a': 100, 'b': 200, 'c': 300, 'd': 600, 'e': 700, 'f': 400, 'g': 900}
list1 = list(d1.values())
list1.sort()
print(list1[len(list1)-3:])

#[600, 700, 900]
