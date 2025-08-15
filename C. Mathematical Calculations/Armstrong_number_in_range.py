#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# A program to find armstrong numbers in range

x=int(input("Enter a range here:"))

for i in range(1,x+1):
    sum=0
    y=len(str(i))
    for j in str(i):
        sum+=(int(j))**y
    if sum==i:
        print(i)
        

