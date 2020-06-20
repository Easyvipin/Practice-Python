# Write a Python script to check whether a given key already exists in a dictionary.

dic1 = {1: 10, 2: 20}


def checkKey(key):
    if key in dic1.keys():  # this will return a list of keys
        print("key exists")
    else:
        print("key does't exists")


checkKey(5)

# key does't exists
