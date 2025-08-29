#!/usr/bin/env python
# coding: utf-8

# In[7]:


x=int(input("Input the starting number of the A.P. series:"))
y=int(input("Input the number of items for the A.P. series:"))
z=int(input("Input the common difference of A.P. series:"))
sum=0

for i in range(y):
    sum+=x
    print(x)
    x+=z
print("The sum of  A.P series:",sum)


# In[ ]:




