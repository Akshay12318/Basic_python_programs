#!/usr/bin/env python
# coding: utf-8

# In[19]:


# A prpgram to find the sum of series[9+99+999+...]

n=int(input("Enter the number of terms:"))
a="9"
sum=0

for i in range(1,n+1):
    term=int(a*i)
    print(term)
    sum+=term
print("The sum of series:",sum)


# 

# In[ ]:




