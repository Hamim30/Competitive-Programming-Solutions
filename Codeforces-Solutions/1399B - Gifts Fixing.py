#!/usr/bin/env python
# coding: utf-8

# In[5]:


for l in range (int(input())):
    input()
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    a_min = min (a)
    b_min= min (b)

    c=[]
    d=[]
    for i in range (len(a)):
        c+=[a[i]-a_min]
        d+=[b[i]-b_min]
    counter =0
    for i in range (len(c)):
        if c[i]==d[i]:
            counter+=c[i]
        elif c[i]>d[i]:
            counter += d[i]
            c[i]-=d[i]
            counter +=c[i]
        elif c[i]<d[i]:
            counter +=c[i]
            d[i] -=c[i]
            counter += d[i]
    print(counter)

