#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Harmonic series-
# The harmonic series is an infinite series in mathematics that sums the reciprocals of all 
# positive integers: 1 + 1/2 + 1/3 + 1/4 + ... and so on.


#Harmonic series and their sum
n=int(input("Enter the number of terms required:"))
sum=0

for i in range(1,n+1):
    print(f"1/{i}")
    sum+=1/i
print("The sum of given Harmonic series is:",round(sum,2))
    





# In[ ]:




