
# coding: utf-8

# In[1]:

bicycles=['trek', 'redline', 'Hero']
print (bicycles)


# In[2]:

print(bicycles[0].title())


# In[4]:

bicycles[0]='Ranger'


# In[5]:

print(bicycles)


# In[6]:

bicycles.append('Trek')


# In[8]:

print(bicycles)


# In[7]:

bicycles.insert(1,'Hercules')


# In[10]:

print(bicycles)


# In[12]:

bicycles.pop()


# In[13]:

print(bicycles)


# In[14]:

bicycles.pop(0)


# In[15]:

print(bicycles)


# In[16]:

cars = ['bmw','audi','toyota','benz']


# In[17]:

print(cars)


# In[ ]:

#Slicing in Python


# In[20]:

Pavan = [1,2,3,4,5,6,7,8,9,10]


# In[21]:

print(Pavan)


# In[22]:

Pavan.slice[4]


# In[23]:

Pavan = Slice[4]


# In[24]:

Pavan[1:3]


# In[25]:

Pavan[0:]


# In[26]:

Pavan[:6]


# In[27]:

Pavan[4:11]


# In[28]:

Pavan[9:29]


# In[21]:

Pavan[0:11:4]


# In[30]:

Pavan[::]


# In[31]:

Pavan[:]


# In[32]:

Pavan[:-1]


# In[33]:

Pavan[::-1]


# In[34]:

print(Pavan)


# In[2]:

Pavan[:0]=[11,12,13]
print(Pavan)


# In[3]:

print(Pavan)


# In[4]:

print(Pavan)


# In[5]:

Pavan


# In[6]:

Pavan = [1,2,3,4,5,6,7,8,9,10]


# In[7]:

print(Pavan)


# In[8]:

Pavan[:0]=[11]


# In[9]:

print(Pavan)


# In[ ]:

# Include new elements in slicing


# In[10]:

Pavan[:0]=[12,12,14,15,16]


# In[11]:

print(Pavan)


# In[12]:

Pavan = Kumar


# In[ ]:

# How to copy a list


# In[13]:

print(Pavan)


# In[14]:

Kumar = Pavan


# In[15]:

print(Kumar)


# In[34]:

for i in range (0,6):
    print (i)
    for j in range (0,5):
        i = i+2


# In[37]:

for i in range (0,6):
    print (i)
    for j in range (0,5):
        i = i+2
        print (i)


# In[44]:

for i in xrange(1,6):
    for j in xrange(1,i+1):
        print "*"
    


# In[ ]:

name = input("What is your name: ")


# In[ ]:

age = int(input("How old are you: "))


# In[ ]:

year = int((2019 - age) + 100)


# In[ ]:

print(name + " will be 100 years old in the year " + year)


# In[1]:

x = 12.2


# In[2]:

y = 14


# In[4]:

print (x)


# In[5]:

x = 100


# In[6]:

print (x)


# In[7]:

z = 9


# In[8]:

z = 9 + 2


# In[9]:

print (z)


# In[10]:

z = z + 3


# In[11]:

print (z)


# In[12]:

p = 5
if p < 10:
    print ('Smaller')
if p > 20:
    print ("Bigger")
print ("Finish")


# In[ ]:

# Tuple data type in Python


# In[13]:

dimensions = (20,50)


# In[14]:

print (dimensions)


# In[15]:

print(dimensions[0])


# In[ ]:

# Lists practice


# In[ ]:

# Declaring a list


# In[16]:

L = [1, 'a', 'string', 1+2]


# In[17]:

print L


# In[18]:

print (L)


# In[ ]:

# Add 6 to the above list, append adds the element at the end of the list


# In[19]:

L.append(6)


# In[20]:

print (L)


# In[ ]:

# pop deletes the last element of the list


# In[21]:

L.pop()


# In[22]:

print (L)


# In[23]:

L.append(9)


# In[24]:

print (L)


# In[ ]:

# Insert is used to add the elements in between the list items


# In[25]:

L.insert(2,22)


# In[26]:

print (L)


# In[27]:

L.insert(3, 11, 12, 13)


# In[28]:

L.insert(3,11)


# In[29]:

print (L)


# In[35]:

L.extend(int(12))


# In[36]:

print (L)


# In[37]:

aList = [123, 'xyz', 'zara', 'abc', 123];


# In[38]:

bList = [2009, 'manni'];


# In[39]:

aList.extend(bList)


# In[57]:

print ('Extended List :', aList)


# In[44]:

print (aList)


# In[45]:

print (bList)


# In[58]:

print (L[1])


# In[ ]:

#For loop in slicing


# In[59]:

players =['kohli','dhoni','yuvaraj','sachin','vijay shankar']


# In[60]:

print('captions of indian team are below')


# In[69]:

for player in players[:2]:
    print (player.title())


# In[70]:

print (players)


# In[64]:

players =['kohli','dhoni','yuvaraj','sachin','vijay shankar']
print (players)


# In[66]:

for player in players:
    print (player.title())


# In[67]:

for player in players[:3]:
    print (player.title()) 
    


# In[68]:

for player in players[:2]:
    print (player.title()) 


# In[71]:

for player in players[:]:
    print (player.title()) 


# In[72]:

for player in players[1:]:
    print (player.title()) 


# In[ ]:



