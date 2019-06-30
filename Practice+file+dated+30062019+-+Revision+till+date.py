
# coding: utf-8

# ## DAY 1 & 2

# In[32]:

#Python
#Variables of Python - User defined 


# In[1]:

var = 10
print(var)


# In[51]:

var1 = 20
var2 = 30
print(var1+var2)


# In[52]:

a = 22.5
b = 30
print (a*b)


# In[53]:

ch1 = 'P'
print (ch1)


# In[54]:

ch2 = 'm'
print (ch2.upper())


# In[55]:

name = 'pavan'
print (name.upper())


# In[56]:

surname = 'BOLLA'
print (surname.lower())


# In[57]:

print(name)


# In[ ]:

#String - It can be defined using single quotes '' or double quotes "" 


# In[ ]:

#String should not have blank spaces while defining, see below:


# In[11]:

full name = 'Pavan Kumar Bolla'


# In[60]:

fullname = 'pavan kumar bolla' #can also use full_name


# In[61]:

print(fullname)


# In[62]:

print(fullname.upper())


# In[63]:

print(fullname.title())


# In[17]:

type(fullname)


# In[19]:

ar1 = 'lilly'


# In[21]:

ar1 = 'jasmine'


# In[22]:

ar1 = 'lavender'


# In[24]:

print (ar1) #prints last defined value


# In[25]:

print (ar1.title())


# In[64]:

ar2 = "is Violet"


# In[65]:

print (ar1.upper() + ' ' + ar2.title())


# ## Day 3

# In[36]:

#Lists - Collection of items
#Lists are mutable - means it can be changed


# In[66]:

bicycles = ['trek', 'redline', 'hero']


# In[70]:

print(bicycles[1])


# In[71]:

#Replacing an element
bicycles[1] = 'Hercules'
print (bicycles)


# In[40]:

#Adding new element
#Can be done using 'insert' or 'append'


# In[72]:

bicycles.append('ranger')
#append is used to add element at the end of the list


# In[74]:

print (bicycles)


# In[75]:

bicycles.insert(1,'LadyBird')
#insert is used to add element at desired index number


# In[78]:

print (bicycles)


# In[79]:

#Deleting a particular element
#Can be achieved using pop()
bicycles.pop()
#Deletes last element


# In[80]:

print (bicycles)


# In[81]:

bicycles.pop(2)
#Deletes particualar index number


# In[82]:

print (bicycles)


# In[ ]:

#Sorting elements in a list using SORT function


# In[83]:

names = ['shyam', 'ramesh', 'abhi', 'anu', 'bhavish']
print (names.sort()) #null


# In[85]:

names.sort()
print (names)


# # Day 4

# In[ ]:

#sorting list in reverse order


# In[86]:

names.reverse()


# In[87]:

print (names)


# In[88]:

cars = ['BMW', 'Audi', 'Toyota','Benz', 'Nissan']


# In[95]:

cars.sort()
print ("Sorted list is")
print (cars)
cars.reverse()
print ("Reverse order is")
print (cars)


# In[96]:

#Creation of empty list


# In[98]:

bikes = []
print ("Initial Blank List")


# In[99]:

print (bikes)


# In[105]:

bikes.append('Yamaha')


# In[106]:

print (bikes)


# In[107]:

bikes.insert(0,'TVS')


# In[108]:

print (bikes)


# In[109]:

bikes.pop(1)


# In[110]:

bikes.pop(0)


# In[112]:

bikes.pop(-1)


# In[113]:

print (bikes)


# In[ ]:

#negative indexing : accesses elements from the end of the list counting backwards


# In[114]:

name = 'Python'


# In[116]:

print (name[-1])


# In[118]:

print (name[-3])


# In[119]:

numbers = [33,21,43,97,23,17,2,65,23,77,19,84,32]


# In[120]:

print (numbers[-3])


# In[121]:

print (numbers[-9])


# In[122]:

print (numbers)


# # Day 5

# In[123]:

#Loops


# In[124]:

print (cars) #we are using list named 'cars' which we created previously


# In[126]:

# FOR LOOP
for car in cars:
    print (car.title())
# title prints 1st letter in upper case


# In[127]:

for car in cars:
    print (car.upper())


# In[129]:

for x in cars:
    print (x.upper())


# In[131]:

# If... else...
num1 = 7
num2 = 0.9
if num1 > num2:
    print ( num1, "is greater")
else:
    print (num1, "is lesser")


# In[132]:

num1 = 7
num2 = 99
if num1 > num2:
    print ( num1, "is greater")
else:
    print (num1, "is lesser")


# In[134]:

# While Loop
i = 1
while i < 7:
    print (i)
    i += 1


# In[137]:

#Print odd numbers between 2 to 20
j = 3
while j < 21:
    print (j)
    j += 2


# In[142]:

#Print even numbers between 1 to 50
k = 2
while k < 50:
    print (k)
    k += 2


# In[ ]:

# While... If... # While... else... # Continue & Break


# In[150]:

i = 0
while i < 11:
    i += 1
    if i == 3:
        continue
    print (i)


# In[1]:

a = 1
while a < 15:
    a += 2
    if a == 9:
        continue
    print (a)


# In[7]:

b = 1
while b < 15:
    b += 2
    if b == 9:
        break
    print (b)


# In[8]:

n1 = 1.2
n2 = 2.9
while n1 > n2:
    print (n1)
else:
    print (n2)


# # Day 6

# In[ ]:

#Slicing of list


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



