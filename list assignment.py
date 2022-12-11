#!/usr/bin/env python
# coding: utf-8

# # sum of all numbers
# # multiplication of all numbers

# In[6]:


s=[2,4,6,8,10]
m=0
n=1
for i in s:
    m+=i
    n*=i
print("sum of numbers is",m)
print("multiplication of numbers is",n)
    


# In[65]:


def is_true(a,b):
    for i in a:
        for j in b:
            if i==j:
                return True
print(is_true([1,2,3,4,5],[4,5,6,7,8]))
print(is_true([1,2,3,5],[4,6,7,8]))


# In[39]:


s=["red", "orange", "green", "blue", "white"]
n= ["black", "yellow", "green", "blue"]
s1=set(s)-set(n)
s2=list(s1)
s3=set(n)-set(s)
s4=list(s3)
print("Color1-Color2: ",s2)
print("Color2-Color1: ",s4)


# In[ ]:




