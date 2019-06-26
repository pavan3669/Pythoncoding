
# coding: utf-8

# In[ ]:

# Tuples


# In[1]:

Dimensions = (500, 600, 700)


# In[2]:

print (Dimensions)


# In[ ]:

# for loop in tuple


# In[10]:

Dimensions = (500, 600, 700)
print("Original dimensions defined")
for dimension in Dimensions:
    print (dimension)
Dimensions = (20,30,40)
print ("\nModified dimensions value")
for dimension in Dimensions:
    print(dimension)


# In[12]:

Dimensions = (500, 600, 700)
print("Original dimensions defined")
print (Dimensions)
Dimensions = (20,30,40)
print ("\nModified dimensions value")
print(Dimensions)


# In[ ]:

# Nested Tuples -- A tuple inside a tuple is called nested tuple (same could be done for lists)


# In[14]:

t3 = ("abc", ("def", "ghi"))


# In[18]:

print (t3)


# In[21]:

t1 = (0, )
t2 = (0, 1, 2, 3)
t3 = 0, 1, 2, 3 #Another four-item tuple (same as prior line, just minus the parenthesis)
t3 = ("abc", ("def", "ghi")) #Nested tuples
#t1[n], t3[n][j] #Index
#t1[i:j] #, Slice
#len(tl) #Length


# In[22]:

print (t1, t2, t3)


# In[25]:

print ("Create/print one tuple")
t1 = 1,2
print (t1)
print ("Create/print another tuple")
t2 = "a","b"
print (t2)


# In[26]:

print ("Create/print nested tuple")
t3 = "A",t1,"B",t2
print (t3)


# In[ ]:

#length of tuple


# In[28]:

print (len(t3))


# In[ ]:

# Sets in Python
# Python program to demonstrate working of Set in Python 


# In[2]:

set1 = set()


# In[3]:

set2 = set()


# In[ ]:

# Adding elements to set1


# In[4]:

for i in range(1,6):
    set1.add(i)


# In[5]:

for i in range(3,8):
    set2.add(i)


# In[6]:

print (set1)
print (set2)


# In[7]:

print ("Set1 = ", set1)
print ("Set2 = ", set2)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



