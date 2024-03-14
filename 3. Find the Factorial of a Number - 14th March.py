#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write your code below
NAME = input("Enter your name ")
CITY = input("Where do you live ? ")
AGE = input("At what age, did you go to college? ")
COLLEGE = input("The college name: ")
PROFESSION = input("What is your profession? ")
PETNAME = input("What will be your pet name? ")

print("There once was a person named " +name+ "who lived in " + CITY + ". At the age of " + AGE + "," + NAME + " went to college at " + COLLEGE + "." + NAME + "graduated and went to work as a " + PROFESSION + ". Then, " + NAME + "adopted an animal named " + PETNAME ". They both lived happily ever after!")


# In[10]:


def factorial(n):     ## recursive approach
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)
p = int(input("Enter a number "))
print(factorial(p))


# In[11]:


def factorial(n):   ## iterative approach
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
 
# Driver Code
num = 5
print("Factorial of",num,"is",
factorial(num))


# In[ ]:





# In[ ]:




