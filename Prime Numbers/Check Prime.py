#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = int(input())
if num > 1: 
    for i in range(2, num//2):  
        if (num % i) == 0: 
            print("Not Prime") 
            break
    else: 
        print("Prime") 
else: 
    print(num, "Not Prime") 

