#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=(1,2,3,2,3,4,5,2,5,4)
b=set(a)
c={}
for i in b:
    c[i]=a.count(i)
c


# In[11]:


b=[("aaaa", 28), ("aa", 30), ("bab", 29), ("bb", 21), ("csa", "C")]
c=b.sort()
c


# In[2]:


def avg(nums):
    result = [sum(x)/len(x) for x in zip(*nums)]
    return result

nums=((1,1,-5),(30,-15,56),(81,-60,-39),(-10,2,3))
avg(nums)


# In[ ]:




