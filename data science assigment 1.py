#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")



# In[2]:


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[3]:


import datetime
now = datetime.datetime.now()

print("Current date and time: ")
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print(now.strftime('%H:%M:%S on %A, %B the %dth, %Y'))


# In[4]:


from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# In[5]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[6]:


a=int(input("enter first number : "))

b=int(input("enter second number : "))

print("sum of",a, "and",b,"is",a+b)

