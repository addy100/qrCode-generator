#!/usr/bin/env python
# coding: utf-8

# In[4]:


## GENERATE qrCode USING PYTHON

import qrcode


# In[6]:


information = 'Hello! Welcome'
qr = qrcode.make(information)
qr.save('Wel.png')
print ('qr Code is generated.')


# In[ ]:





# In[ ]:




