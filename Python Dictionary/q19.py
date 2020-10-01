# Write a Python program to combine values in python list of dictionaries.

itemList = [{'item': 'item1', 'amount': 400}, {
    'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
commonDic = {}

for i in itemList:
    if i['item'] in commonDic.keys():
        commonDic[i['item']] += i['amount']
    else:
        commonDic[i['item']] = i['amount']

print(commonDic)

#{'item1': 1150, 'item2': 300}
