# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

dic = {}
n = 5
for item in range(1, 5+1):
    dic[item] = item * item

print(dic)

#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
