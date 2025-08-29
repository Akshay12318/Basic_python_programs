#!/usr/bin/env python
# coding: utf-8

# In[1]:


# sum and average of natural numbers within the given range

sum=0
count=0
n=int(input("Enter a range here :"))
for i in range(1,n+1):
    sum+=i
    count+=1
print("The sum of given numbers :",sum)
print("The average of given numbers :",sum/count)
    


# In[ ]:




