#!/usr/bin/env python
# coding: utf-8

# In[4]:


principal = int(input("Enter the principal amount "))
rate = float(input("Enter the rate "))
time = int(input("Enter the time span "))

amount = principal * (pow((1 + rate / 100), time))
CI = amount - principal
print("The compound interest is ", CI)


# In[5]:


def compound(principal,rate,time):
    amount = principal * (pow((1 + rate / 100), time))
    return amount - principal
print(compound(10000,10,5))


# In[7]:


# Python3 program to find compound
# interest for input taking from user.


def compound_interest(principal, rate, time):

	# Calculates compound interest
	Amount = principal * (pow((1 + rate / 100), time))
	CI = Amount - principal
	print("Compound interest is", CI)


# Driver Code
#Taking input from user.
principal = int(input("Enter the principal amount: "))
rate = float(input("Enter rate of interest: "))
time = int(input("Enter time in years: " ))
#Function Call
compound_interest(principal,rate,time)

