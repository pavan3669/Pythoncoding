
# coding: utf-8

# In[ ]:

#Modules: Used to hide core business logic
#A module is a Python object with arbitrarily named attributes that you can bind and reference. 
#Simply, a module is a file consisting of Python code. A module can define functions, classes and variables. 
#A module can also include runnable code.


# In[4]:

import numpy as np
import math_logic

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

vec1 = np.array([x,y])
vec2 = np.array([-x,-y])

answer1 = math_logic.add(x,y)
answer2 = math_logic.sub(x,y)
answer3 = math_logic.mult(x,y)

print(answer1)
print(answer2)
print(answer3)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



