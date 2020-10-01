#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = int(input())
n = 1
k = 1
for i in range(0, num):
    for j in range(num, i, -1):
        print(n, end=" ")
        n = n + 1
    while k < 2*i:
        print("*",end=" ")
        k = k+1
    print()
    n = 1
    k = 1


# In[ ]:




