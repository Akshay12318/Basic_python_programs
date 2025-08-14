#!/usr/bin/env python
# coding: utf-8

# In[8]:


# A program that displays the n terms of Square Natural Numbers and Their Sum.1 4 9 16 n...

n=int(input("Enter the number of terms:"))
sum=0

print(f"The square natural numbers upto {n} terms :")
for i in range(1,n+1):
    print(i**2,end=" ")
    sum+=(i**2)
print("\nThe sum of Square natural numbers:",sum)


# In[ ]:




