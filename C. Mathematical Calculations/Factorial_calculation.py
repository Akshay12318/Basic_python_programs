#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Factorial calculation- using Recursion

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
a=int(input("Enter a number to find Factorial:"))
factorial(n=a)

# Explanation
# 1)Function calls itself with n-1
# 2)stops at base case n==0
# 3)Multiple results backward to get final value



# In[ ]:




