#!/usr/bin/env python
# coding: utf-8

# In[22]:


n = int(input("Enter a number "))
s = n
sum_ = 0
while n != 0:
    rem = n%10
#     power = pow(rem,3)
    sum_ = sum_ + pow(rem,3)  ##power
    n = n//10
print(sum_)

if s == sum_:
	print("The given number", s, "is armstrong number")
else:
	print("The given number", s, "is not armstrong number")


# In[18]:


pow(5,2)


# In[14]:


n = 153 # or n=int(input()) -> taking input from user
s = n # assigning input value to the s variable
b = len(str(n))
sum1 = 0
while n != 0:
	r = n % 10
	sum1 = sum1+(r**3)
	n = n//10
if s == sum1:
	print("The given number", s, "is armstrong number")
else:
	print("The given number", s, "is not armstrong number")

