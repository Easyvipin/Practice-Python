#!/usr/bin/env python
# coding: utf-8

# In[ ]:
    
    
'''
check_prime returns true if the given number is prime else it returns false.
'''
def check_prime(number):
    if(number <= 1):
        return False
    
    for i in range(2, number//2):
        if(number % i) == 0:
            return False
    return True

number  = int(input("Enter the number: "))

if(check_prime(number)):
    print("Number is Prime")
else:
    print("Number is not Prime")
