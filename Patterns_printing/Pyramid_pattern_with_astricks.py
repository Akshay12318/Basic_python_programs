#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Pyramid pattern with astricks
    
x="*"
n=" "
a=int(input("Enter a range here :"))

for i in range(1,a+1):
    print(n*(a-i),end=" ")
    for j in range(i):
        print(x,end=" ")
    print()
    



# In[ ]:




