#!/usr/bin/env python
# coding: utf-8

# In[7]:


a = int(input("Write the first number "))
b = int(input("Write second first number "))
c = a + b
print("The sum is ",c)


# In[ ]:





# In[8]:


def add(a,b):
    return a+b
p = int(input("Write the first number "))
q = int(input("Write second first number "))
print(add(p,q))


# In[13]:


def add(a,b):
    return a+b
p = float(input("Write the first number ")) #if both are integer input, sum won't happen
q = int(input("Write second first number "))

sum_of_twonumbers = add(p,q)
#To print the result
print("Sum of {0} and {1} is {2}" .format(p,
                           q, sum_of_twonumbers))

