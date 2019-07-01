
# coding: utf-8

# In[ ]:

# Libraries
# User defined declarations
# Files & Exception handling - Core Python
# How to achieve user inputs.. while running a program: input()


# In[1]:

message = input ("Tell me someting and I will repeat it back to you:")
print (message)


# In[3]:

name = input ("Please enter your name:")
print (f"\n Hello, {name}!") #{name} is called place holder in this case


# In[4]:

name_1 = input ("Please enter your age:")
print (f"\n Your age is: {name_1}")


# In[5]:

is name_1 > 20 # Python considers each element as str unless its declared. In this case age is int however its considered as str
# str input() always gives output as str only


# In[6]:

name_2 = int(name_1)


# In[9]:

print (name_2)


# In[11]:

if (type(name_2) is int):
    print ("Int")
else:
    print (type(name_2))


# In[12]:

if (type(name_2) is int):
    print ("True")
else:
    print ("False")


# In[13]:

is (name_2) > 20 


# In[ ]:



