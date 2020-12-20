#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
print(np.__version__)


# In[2]:


import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)


# In[3]:


#Create a 0-D array with value 42
import numpy as np
arr = np.array(42)
print(arr)


# In[4]:


#Create a 1-D array containing the values 1,2,3,4,5:
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)


# In[5]:


#reate a 2-D array containing two arrays
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


# In[6]:


#Create a 3-D array with two 2-D arrays,
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)


# In[7]:


#Get the first element
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])


# In[8]:


#Get the second element
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[1])


# In[9]:


#Get third and fourth elements
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])


# In[10]:


#Access the third element of the second array of the first array:
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])


# In[11]:


#Slice from the index 3 from the end to index 1 from the end
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])


# In[12]:


#Return every other element from index 1 to index 5
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])


# In[13]:


#Get the data type of an array object:
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)


# In[14]:


#Get the data type of an array containing strings:
import numpy as np
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)


# In[15]:


#Create an array with data type string:
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)


# In[16]:


#Print the shape of a 2-D array:
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)


# In[17]:


#Create an array with 5 dimensions using ndmin
import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)


# In[18]:


#Convert the following 1-D array with 12 elements into a 2-D array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)


# In[19]:


#Convert the following 1-D array with 12 elements into a 3-D array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)


# In[20]:


#Convert 1D array with 8 elements to 3D array with 2x2 elements
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)


# In[21]:


#Join two arrays
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)


# In[22]:


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)


# In[23]:


#Split the array in 3 parts
import numpy as np
arr = np.array([1, 2, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)


# In[24]:


#Split the 2-D array into three 2-D arrays along rows
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)


# In[25]:


#Find the indexes where the value is 4:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)


# In[26]:


#Find the indexes where the values are even:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 7, 8])
x = np.where(arr%2 == 0)
print(x)


# In[27]:


#Find the indexes where the values are odd:
import numpy as np
arr = np.array([1, 2, 3, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x)


# In[28]:


#Find the indexes where the values 2, 4, and 6 should be inserted:
import numpy as np
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)


# In[29]:


#Sort the array:
import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))


# In[30]:


#ort the array alphabetically:
import numpy as np
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))


# In[31]:


#Sort a boolean array:
import numpy as np
arr = np.array([True, False, True])
print(np.sort(arr))


# In[32]:


#Sort a 2-D array:
import numpy as np
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))


# In[33]:



#Create an array from the elements on index 0 and 2:
import numpy as np
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)


# In[34]:


#Sort a boolean array:
import numpy as np
arr = np.array([True, False, True])
print(np.sort(arr))


# In[35]:



#Create a filter array that will return only values higher than 42:
import numpy as np
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


# In[36]:


#Generate a random integer from 0 to 100:
from numpy import random
x = random.randint(100)
print(x)


# In[37]:


#Generate a 1-D array containing 5 random integers from 0 to 100:
from numpy import random
x=random.randint(100, size=(5))
print(x)


# In[38]:


#Generate a 2-D array with 3 rows, each row containing 5 random numbers:
from numpy import random
x = random.rand(3, 5)
print(x)


# In[39]:


from numpy import random
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)


# In[40]:


#Randomly shuffle elements of following array:
from numpy import random
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)


# In[41]:


#Convert following array with repeated elements to a set:
import numpy as np
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)


# In[42]:


#Reshaping an array into two rows:
a = np.arange(100)
b = np.reshape(a, (2, -1))
b


# In[43]:


#Find sine values for all of the values in arr:
import numpy as np
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)


# In[ ]:




