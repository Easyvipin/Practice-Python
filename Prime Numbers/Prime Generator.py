#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import sqrt
for _ in range(int(input())):
    a,b = map(int,input().split())
    num_prime = {}
    
    for i in range(2,int(sqrt(b)+1)):
        for j in range(max(a//i,2),(b//i)+1):
            num_prime[i*j] = 1
    
    for i in range(max(a,2),b+1):
        if i not in num_prime:
            print(i,end=" ")
    print()   

