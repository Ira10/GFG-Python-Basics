#!/usr/bin/env python
# coding: utf-8

# In[3]:


principal_amt = int(input("Enter the principal amount "))
time = int(input("Enter the years "))
rate = int(input("Enter the rate of the interest"))

interest = (principal_amt * time * rate) /100

print("The interest is ",interest)

