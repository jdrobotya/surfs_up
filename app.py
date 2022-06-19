#!/usr/bin/env python
# coding: utf-8

# In[12]:


from flask import Flask


# In[13]:


app = Flask(__name__)


# In[14]:


@app.route('/')
def hello_world():
    return 'Hello world'


# In[ ]:





# In[ ]:




