# Write a Python program to select an item randomly from a list.

import random

list1 = ["vipin", "123 street", "india"]

randItem = list1[random.randint(0, len(list1)-1)]
print(randItem)
