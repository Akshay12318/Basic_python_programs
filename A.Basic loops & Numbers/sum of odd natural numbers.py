#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Odd Natural Numbers and Their Sum for n no. of terms required

n=int(input("Enter a range here :"))
sum=0
print("The odd numbers are :")
for i in range(1,2*n):
    if i%2==0:
        continue
    print(i,end=" ")
    sum+=i
print(f"\nThe sum of odd numbers :{sum}")   #use of escape sequence


# In[ ]:




