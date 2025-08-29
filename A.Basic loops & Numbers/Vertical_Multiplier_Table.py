#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Vertical multiplier table from 1 to n

n=int(input("Enter a table range here :"))

for i in range(1,n+1):
    for j in range(1,11):
        print(f"{j} x {i} = {i*j}",end=" | ")
    
    print()


# In[ ]:




