#!/usr/bin/env python
# coding: utf-8

# In[ ]:

num = int(input("Enter the number\n"))
if num > 1:
	for i in range(2,num):
		if (num % i) ==0:
			print(num,"is  a prime number")
			break
	else:
			print(num,"is not a prime number")

			exit()
