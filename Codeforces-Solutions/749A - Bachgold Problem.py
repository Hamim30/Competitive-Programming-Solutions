#!/usr/bin/env python
# coding: utf-8

# In[12]:


a= int(input())
c=0
if a%2==0:
    x="2 "*int(a/2)
    c=int(a/2)
    print(c)
    print(x.strip())
else:
    a-=3
    c=int(a/2)+1
    print(c)
    print("2 "*int(a/2)+"3")

