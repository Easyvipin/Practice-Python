# wap picnic table through ljust, rjust, center\


def picnicTable(picnicItems, leftWidth, rightWidth):
    print('Picnic Items'.center(leftWidth + rightWidth, "-"))
    for key, value in picnicItems.items():
        print(key.ljust(leftWidth, ".") + str(value).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
picnicTable(picnicItems, 20, 5)

""" -------PICNIC ITEMS-------
sandwiches.......... 4
apples.............. 12
cups................ 4
cookies............. 8000 """
