#!/usr/bin/env python
# coding: utf-8

# In[10]:


x="*"
y=" "
n=int(input("Enter a range here :"))

for i in range(1,n+1):
    print(y*(n-i),end="")
    for j in range(i):
        print(x,end=" ")
    print()

for k in range(n-1,0,-1):
    print(y*(n-k),end="")
    for l in range(k):
        print(x,end=" ")
    print()


# In[ ]:




