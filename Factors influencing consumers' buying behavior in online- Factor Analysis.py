#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from factor_analyzer import FactorAnalyzer


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


df= pd.read_excel("Data.xlsx")


# In[5]:


pwd()


# In[6]:


import os


# In[7]:


os.chdir("D:\IBS\Signature Courses - IBS\mounika")


# In[8]:


pwd()


# In[9]:


df= pd.read_excel("Data.xlsx")


# In[10]:


df.columns


# In[11]:


df.dropna(inplace=True)


# In[12]:


df.info()


# In[13]:


df.head()


# In[14]:


from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
chi_square_value,p_value=calculate_bartlett_sphericity(df)
chi_square_value, p_value


# In[15]:


from factor_analyzer.factor_analyzer import calculate_kmo
kmo_all,kmo_model=calculate_kmo(df)


# In[16]:


kmo_model


# In[17]:


fa = FactorAnalyzer()


# In[18]:


fa.analyze(df, 25, rotation=None)


# In[19]:


fa.analyze(df, 15, rotation=None)


# In[20]:


ev, v = fa.get_eigenvalues()


# In[21]:


ev


# In[22]:


plt.scatter(range(1,df.shape[1]+1),ev)


# In[23]:


plt.plot(range(1,df.shape[1]+1),ev)


# In[24]:


plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()


# In[25]:


plt.scatter(range(1,df.shape[1]+1),ev)
plt.plot(range(1,df.shape[1]+1),ev)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()


# In[26]:


fa = FactorAnalyzer()


# In[27]:


fa.analyze(df, 5, rotation="varimax")


# In[28]:


fa.loadings


# In[29]:


fa = FactorAnalyzer()
fa.analyze(df, 4, rotation="varimax")
fa.loadings


# In[30]:


fa.get_factor_variance()


# In[31]:


fa = FactorAnalyzer()
fa.analyze(df, 5, rotation="varimax")
fa.loadings


# In[32]:


fa.get_factor_variance()


# In[ ]:




