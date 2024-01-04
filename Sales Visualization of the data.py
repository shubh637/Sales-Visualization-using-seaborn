#!/usr/bin/env python
# coding: utf-8

# In[288]:


#importing all libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[289]:


df=pd.read_csv("C:\\Users\\TUSHAR SAIN\\Downloads\\Diwali Sales Data.csv",encoding="unicode_escape")
df.head()


# In[290]:


df.info()


# In[291]:


df.describe()


# In[292]:


df.isnull().sum()


# In[293]:


#cleaning the data
df.drop(["Status","unnamed1"],axis=1,inplace=True)


# In[294]:


df["Amount"].fillna(df["Amount"].mode()[0],inplace=True)


# In[295]:


df.isnull().sum()


# In[296]:


df["Amount"]=df["Amount"].astype("int")
df.head()


# In[297]:


df["Amount"].dtypes
df.shape


# In[298]:


#Exploratory Data Analysis
ax=sns.countplot(x="Gender",data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[299]:


#purchased done by the female and male
sales_gen=df[["Amount"]].groupby(df["Gender"]).sum()
sales_gen
sns.barplot(x=sales_gen.index,y=sales_gen["Amount"])


# In[300]:


ax=sns.countplot(x=df["Age Group"],hue=df["Gender"])
for bars in ax.containers:
    ax.bar_label(bars)


# In[301]:


# total Amount vs Age Group
sales_age=df[["Amount"]].groupby(df["Age Group"]).sum()
sns.barplot(x=sales_age.index,y=sales_age["Amount"])


# In[302]:


#total number of oreder from top 10 states
sales_state=df[["Orders"]].groupby(df["State"]).sum().sort_values(by=["Orders"],ascending=False)
sns.set(rc={"figure.figsize":(25,5)})
sns.barplot(x=sales_state.index,y=sales_state["Orders"])


# In[303]:


#marital Status
ax=sns.countplot(x=df["Marital_Status"])
sns.set(rc={"figure.figsize":(10,5)})
for bar in ax.containers:
    ax.bar_label(bar)


# In[304]:


sales_state=df[["Amount"]].groupby(df["Marital_Status"]).sum().sort_values(by=["Amount"],ascending=False)
sns.set(rc={"figure.figsize":(10,7)})
sns.barplot(x=sales_state.index,y=sales_state["Amount"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




