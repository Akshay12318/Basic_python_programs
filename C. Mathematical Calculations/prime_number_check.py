#!/usr/bin/env python
# coding: utf-8

# In[3]:


x=int(input("Enter a number here:"))

if x<2:
    is_prime=False
else:
    is_prime=True
    for i in range(2,x):
        if x%i==0:
            is_prime=False
            break
if is_prime:
    print("It is a prime number")
else:
    print("It is not a prime number")


# In[ ]:




