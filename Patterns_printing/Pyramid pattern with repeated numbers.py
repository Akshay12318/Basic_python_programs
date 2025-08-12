#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Pyramid pattern with repeated numbers

x=" "
n=int(input("Enter a range here :"))

for i in range(1,n+1):
    print(x*(n-i),end="")
    for j in range(i):
        print(i,end=" ")
    print()


# In[ ]:




