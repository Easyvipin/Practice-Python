# program based on keys(), values(), and items() Methods

spam = {'color': 'red', 'age': 42}
print(list(spam.keys()))

#['color', 'age']

for eachKey in spam.keys():
    print(eachKey)
# color
# age

# items
for eachKey, eachValue in spam.items():
    print(eachKey, eachValue)

# color red
# age 42

# values
for eachValue in spam.values():
    print(eachKey)
# red
# 42
