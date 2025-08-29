#!/usr/bin/env python
# coding: utf-8

# In[7]:


# A geometric progression (GP), or geometric sequence, is a sequence of non-zero numbers where each term after the first is found 
# by multiplying the previous term by a fixed, non-zero number called the common ratio (r).
# The general form of a GP is a, ar, ar², ar³, ...,

x=int(input("Enter a 1st number:"))
y=int(input("Enter the number of terms:"))
r=int(input("Enter the common ration of the G.P. series"))

print("\nThe terms are as follows :")
for i in range(y):
    print(x*((r)**i))


# In[ ]:




