#!/usr/bin/env python
# coding: utf-8

# In[1]:
## GENERATE qrCode USING PYTHON
import qrcode

# In[2]:
information = 'Hello! Welcome'
qr = qrcode.make(information)
qr.save('Wel.png')
print ('qr Code is generated.')
