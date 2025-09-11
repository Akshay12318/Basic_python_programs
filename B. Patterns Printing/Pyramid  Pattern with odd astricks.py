#!/usr/bin/env python
# coding: utf-8

# In[11]:


#pyramid  Pattern with odd astricks

x=" "
a="*"
n=int(input("Enter a range here:"))*2

for i in range(1,n+1):
    print(x*(n-i),end="")
    for j in range(i):
        if i%2!=0:
            print(a,end=" ")
    print()


# In[ ]:




