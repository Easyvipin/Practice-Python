#  Write a Python program to print all unique values in a dictionary.
d1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
      {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
uniqueList = []
for i in range(0, len(d1)):
    for value in list(d1[i].values()):
        if value not in uniqueList:
            uniqueList.append(value)

uniqueDic = set(uniqueList)
print(uniqueDic)

# {'S002', 'S001', 'S009', 'S007', 'S005'}
