#!/usr/bin/env python
# coding: utf-8

# In[7]:


# count uppercase,lowercase & other characters

x=input("Enter:")
upper=0
lower=0
other=0

for i in x:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    else:
        other+=1
        
print("Upper characters count:",upper)
print("Lower characters count:",lower)
print("Other characters count:",other)


# In[ ]:




