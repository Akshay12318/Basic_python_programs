#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Armstrong number check
# Armstrong numbers are numbers that are equal to the sum of their digits each raised to the power of the number of digits.

x=input("Enter a number here to check:")
y=len(x)
sum=0

for num in x:
    sum+=int(num)**y
if int(x)==sum:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")
    


# In[ ]:




