#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Alternate sum series[x-x3+x5-....]

x=int(input("Enter value of x:"))
n=int(input("Enter the number of terms required:"))
a=1
sign=1
for i in range(1,n+1):
    print((x*sign)**a)
    a+=2
    sign*=-1
    


# In[ ]:




