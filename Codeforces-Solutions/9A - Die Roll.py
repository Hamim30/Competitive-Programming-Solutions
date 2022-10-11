#!/usr/bin/env python
# coding: utf-8

# In[16]:


a=[int(i) for i in input().split()]
m=max(a)
if m==1:
    print("1/1")
elif m ==2:
    print("5/6")
elif m ==3:
    print("2/3")
elif m==4:
    print("1/2")
elif m==5:
    print("1/3")
else:
    print("1/6")

