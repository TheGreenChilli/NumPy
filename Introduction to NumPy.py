#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

a = np.array([20,30,40])
b = np.array([4])
print(a)
print(b)
print(a*b)


# In[4]:


a = np.array([40,50,60.0])
print(a)


# In[10]:


l1 = [20, 30,40]
l2 = 5
print(l1*l2)


# In[15]:


import numpy as np

arr = np.array([10,20,30,40])

print(arr)
print(type(arr))


# In[19]:


arr = np.array([[10,20,30],[50,60,70],[80,90,10]])
print(arr)


# In[24]:


# slicing

arr = np.array([10,20,30,40])
print(arr[0:3])
print(arr[3:])
print(arr[2:])
print(arr[:3])


# In[28]:


arr = np.array([[10,20,30,40],[50,60,70,80]])
print(arr[0:2,0:2])
print(arr[0,1:3])
print(arr[1,2:4])


# In[33]:


arr = np.array([[10,20,30,40],[40,50,60,70],[70,80,90,10]])
print(np.shape(arr))
print(np.size(arr))
print(np.ndim(arr))
print(arr.dtype)


# In[7]:


import numpy as np

a = [[30,40,40],[40,30,10]]
arr = np.array(a)
print(arr)
print(arr.shape)  #rows,columns
print(len(arr))    #number of nested values
print(np.size(arr))   #number of elements
print(type(arr))      #datatype of variable
print(arr.dtype)      #datatype of array
print(arr.astype(float)) #conversion of datatype


# In[8]:


# addition 

import numpy as np
arr1 = np.array([[30,40],[20,10]])
arr2 = np.array([[30,40],[20,10]])
print(arr1+arr2)
print(np.add(arr1,arr2))


# In[9]:


# subtraction

import numpy as np
arr1 = np.array([[30,40],[20,10]])
arr2 = np.array([[30,40],[20,10]])
print(arr1-arr2)
print(np.subtract(arr1,arr2))


# In[10]:


# multiplication 

import numpy as np
arr1 = np.array([[30,40],[20,10]])
arr2 = np.array([[30,40],[20,10]])
print(arr1*arr2)
print(np.multiply(arr1,arr2))


# In[11]:


# divide

import numpy as np
arr1 = np.array([[30,40],[20,10]])
arr2 = np.array([[30,40],[20,10]])
print(arr1/arr2)
print(np.divide(arr1,arr2))


# In[12]:


# power

import numpy as np
arr1 = np.array([3, 4,2,1])
arr2 = np.array([2])
print(np.power(arr1,arr2))


# In[15]:


# square

arr1 = np.array([9, 16, 4, 1])
print(np.sqrt(arr1))


# In[4]:


# concatenate

import numpy as np
arr1 = np.array([30,40,50])
arr2 = np.array([5,5,3])
print(np.concatenate([arr1,arr2]))


# In[5]:


arr1 = np.array([[30,40],[50,10]])
arr2 = np.array([[5,5],[3,3]])
print(np.concatenate([arr1,arr2],axis = 0))


# In[7]:


# horizontal, vertical
print(np.hstack([arr1,arr2]))
print(np.vstack([arr1,arr2]))


# In[10]:


# split
a = np.array([20,40,30,40,10,20])
b = np.array_split(a,3)
print(b[1])


# In[11]:


a = np.array([20,40,30,40,10,20])
b = np.array_split(a,5)
print(b) 


# In[13]:


a = np.array([[20,40,30],[40,10,20]])
b = np.array_split(a,3)
print(b) 


# In[14]:


# append
a = np.array([20,30,40])
print(np.append(a,50))


# In[17]:


a = np.array([[20,30],[40,50]])
print(np.append(a,[60,70]))


# In[19]:


# insert
print(np.insert(a,1,50))
print(np.insert(a,1,[50,60], axis = 1))


# In[20]:


print(np.insert(a,[1,2],[50,60], axis = 0))  #for multiple indexes


# In[25]:


# delete
a = np.array([[20,40],[60,80]])
print(np.delete(a,1))
print(np.delete(a,1, axis = 0))


# In[28]:


# sort

ar = np.array([7,8,4,12,9])
print(np.sort(ar))

ar = np.array([[7,8,4,12,9],[2,8,5,1,3]])
print(np.sort(ar))


# In[30]:


# search

ar = np.array([3,4,1,7,8])
s = np.where(ar%2 == 0)
print(s)

ar = np.array([1,2,3,4,5]) #to find index
ss = np.searchsorted(ar,5)
print(ss)


# In[38]:


# filter

import numpy as np

ar = np.array([20,30,40,50])
fa = (True, False, False, False)
new = ar[fa]
print(new)


# In[37]:


ar = np.array([20,30,40,50])
fa = ar>35
new = ar[fa]
print(new)


# In[41]:


a = np.array([20,40,60,70])

print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.size(a))
print(np.mean(a))
print(np.cumsum(a)) #cumulative sum
print(np.cumprod(a))    #cumulative product


# In[47]:


a = [100,150,199,200,250,130]
b = [10,50,30,40,30,10]

price = np.array(a)
quantity = np.array(b)

print(price, "\n", quantity)
print()
c = np.cumprod([price,quantity], axis = 0)
print(c[1].sum())


# In[54]:


# statistical functions in arrays

import numpy as np
import statistics as stats
baked_food = [200,300,150,130,200,280,170,188]

a = np.array(baked_food)
print(np.mean(baked_food))    #sum of all the values/number of values
print(np.median(baked_food))  #central value after sorting
print(stats.mode(baked_food))
print(np.std(baked_food))
print(np.var(baked_food))
 


# In[56]:


# -1 represents inversaly proportional relationship
#  1 represents proportional relationship
# 0 means no relationship
tobacco_consumption = [30,50,10,30,50,40]
deaths = [100,120,70,100,120,112]

print(np.corrcoef([tobacco_consumption,deaths]))


# In[57]:


price = [300,100,350,150,200]
sales = [10,20,7,17,3]

print(np.corrcoef([price,sales]))


# In[ ]:




