#!/usr/bin/env python
# coding: utf-8

# In[17]:


# A python program tat converts a given number of days into years,weeks and days

x=int(input("Enter a Days here:"))

years=x//365
weeks=(x-years*365)//7
days=x-(years*365)-(weeks*7)
print(f"The Years are :{years},\nThe weeks are :{weeks},\nThe Days are  :{days}")
    


# In[ ]:




