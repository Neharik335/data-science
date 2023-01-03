#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# # - Combine visits and cart using a left merge.
# - How long is your merged DataFrame?
# - How many of the timestamps are null for the column cart_time?
# - What percent of users who visited site ended up not placing a t-shirt in their cart?
# - Repeat the left merge for cart and checkout and count null values. What percentage of users put items in their cart, but did not proceed to checkout?

# In[5]:


check=pd.read_csv(r"C:\Users\Admin\Downloads\checkout.csv")
cart=pd.read_csv(r"C:\Users\Admin\Downloads\cart.csv")
visit=pd.read_csv(r"C:\Users\Admin\Downloads\visits.csv")
pur=pd.read_csv(r"C:\Users\Admin\Downloads\purchase.csv")


# In[6]:


cart


# In[7]:


visit


# In[31]:


df=pd.merge(visit,cart,how="left")
df


# In[16]:


df.shape


# In[32]:


df.cart_time.isna().value_counts()


# In[33]:


cart


# In[34]:


visit


# In[35]:


pur


# In[37]:


df1=pd.merge(visit,cart,how="outer")
df1


# In[38]:


df1.cart_time.isna().value_counts()


# In[39]:


v=visit.user_id.count()
v


# In[44]:


per=(1652/v)*100
print("percent of users who visited site ended up not placing a t-shirt in their cart: ",per)


# In[47]:


df3=pd.merge(cart,check,how="left")
df3


# In[50]:


df3.isna().value_counts()


# In[52]:


b=cart.user_id.count()
b


# In[55]:


per=(122/b)*100
print("percentage of users put items in their cart, but did not proceed to checkout:",per)


# In[ ]:




