#!/usr/bin/env python
# coding: utf-8

# All test cases passed

# In[1]:


num = int(input())
n = 1
k = num
for i in range(0, num):
    for j in range(0, i+1):
        print(n, end="")
        n = n + 1
    while k > i+1:
        print("*",end = "")
        k = k-1
    print()
    n = 1
    k = num


# In[ ]:




