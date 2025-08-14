#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Perfect number-
# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself

n=int(input("Enter a number here:"))
sum=0

for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("It is a Perfect number")
else:
    print("It is not a perfect number")


# In[ ]:




