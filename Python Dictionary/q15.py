# Write a Python program to combine two dictionary adding values for common keys.

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
commonDic = {}
for key in list(d1.keys()):
    if key in d2:
        commonDic[key] = d1[key] + d2[key]

print(commonDic)

# {'a': 400, 'b': 400}
