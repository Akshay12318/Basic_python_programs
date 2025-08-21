#!/usr/bin/env python
# coding: utf-8

# In[4]:


x=int(input("Enter a range here"))

if x<2:
    is_prime=False
else:
    for i in range(2,x+1):
        is_prime=True
        for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            print(i)
    


# In[ ]:




