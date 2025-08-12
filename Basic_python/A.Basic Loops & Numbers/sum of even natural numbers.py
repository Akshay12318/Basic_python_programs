#!/usr/bin/env python
# coding: utf-8

# In[5]:


# sum of even natural numbers for a given number of terms

n=int(input("Enter a number of terms here:"))
sum=0

for i in range(2,(2*n)+2):
    if i%2==0:
        print(i)
        sum+=i
print("\nThe sum of Even numbers is :",sum)



# In[ ]:




