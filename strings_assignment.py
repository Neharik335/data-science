#!/usr/bin/env python
# coding: utf-8

# In[5]:


a="hEllo"
b=a.lower()
b


# In[51]:


a="PYTHON"
b=""

for i in range(len(a)):
    if i%2!=0:
        b=b+a[i].lower()
    else:
        b=b+a[i].upper()
b
    
    


# In[48]:


a="PYTHON"
c=" "
for i in range(len(a)):
    if i%2==0:
        c=c+a[i].lower() 
        
    else:
        c=c+a[i].upper()
c


# In[52]:


a="PYTHON"
c=" "
for i in range(len(a)):
    if i%2==0:
        c=c+a[i].lower() 
        
    else:
        c=c+a[i].upper()
c


# In[53]:


a="PYTHON"
c=" "
for i in range(len(a)):
    if i%2==0:
        c=c+a[i].upper() 
        
    else:
        c=c+a[i].lower()
c


# In[56]:


c={"name":"neharika", "gender":"female", "age":21, "phone number":45, "father name":"srini","mom":"ran"}
biodata=print("my name is",c["name"],"my age is",c["age"],"my phone no is",c["phone number"],"and my father name is",c["father name"],"my mom name is ",c["mom"] )


# In[57]:


e="S@ndhy@"
e.count("@")


# In[76]:


s="name1.@gmail.com, name2.@gmail.com, name3.@gmail.com"
c=s.split(".@gmail.com")


# In[95]:


a='abcdefghijklmnopqrstuvwxyz'
d=['a','e','i','o','u']
e=""
for i in a:
    if i not in d:
        e=e+i
print(e)


# In[99]:


b="Welcome to Innomatics. innomatics awesome, isn't it?"
c=b.lower()
d=c.count("innomatics")
print(" The innomatics count is:",d)


# In[ ]:




