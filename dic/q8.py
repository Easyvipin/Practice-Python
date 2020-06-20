# Write a Python script to concatenate following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

concatDic = list(dic1.items()) + list(dic2.items()) + list(dic3.items())
print(concatDic)
allDic = dict(concatDic)
print(allDic)
