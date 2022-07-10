#!/usr/bin/env python
# coding: utf-8

# In[12]:


# To Print the Astrix
def pypart(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")
pypart(5)


# In[13]:


# Program to remove characters from a string
chars = [';', ':', '!', "*",'#']
a = input("Enter the string: ")
print ("Original string : " , a)
for i in chars :
    a = a.replace(i, '')
print ("Characters removed string : " , str(a))


# In[5]:


# Iterate the given list of numbers and print only those which are divisible by 5
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in x:
    if(i%5 == 0):
        print("The value is :",i)
    else :
        continue


# In[15]:


# Find Number of times "Hi" is printed in a string
a = input("Enter the string:")
b = "Hi"
print("Number of times the word 'Hi' is displayed in the given string : ", a.count(b))        


# In[16]:


# Print the Following Pattern
rows = 6
for i in range(rows):
    
    for j in range(i):
        print(i, end=' ')
    print('')


# # List Exercises:

# In[19]:


# Interchanging First and Last element
a = [1,2,3,4,5]
print("Before Interchanging:",a)
x = a[0]
y = a[-1]
a.pop()
del a[0]
a.append(x)
a.insert(0,y)
print("After Interchanging: ",a)


# In[7]:


# Swap two elements in a list
def swap(s1,pos1,pos2):
    n = len(s1)
    temp = s1[pos1]
    s1[pos1] = s1[pos2]
    s1[pos2] = temp
    return s1
a = [5,2,3,4,1]
pos1 = int(input("Enter element 1 : "))
pos2 = int(input("Enter element 2 : "))
print("The list:",a)
print("Swapped list:",swap(a,pos1-1,pos2-1))


# In[1]:


# Ways to find the length of list
x = [1,2,3,4,5,6]
y = x.__len__()
print("The length of the list =",y)


# In[22]:


# Maximum of two numbers
def max(a, b):
    if a >= b:
        return a
    else:
        return b
a = int(input("Enter a : "))
b = int(input("Enter b : "))
print("Maximum =",max(a, b))


# In[23]:


# Minimum of two numbers 
def min(a, b):
    if a <= b:
        return a
    else:
        return b
a = int(input("Enter a : "))
b = int(input("Enter b : "))
print("Minimum =",min(a, b))


# # String Exercises:

# In[24]:


# Check the string whether it is Symmetrical or Palindrome
a = input("Enter the string:")
x = a[::-1]
if a==x:
    print("The given string is Pallindrome")
else:
    print("The given string is Symmetrical")


# In[25]:


# Reverse Strings
a = input("Enter the word: ")
x = a[::-1]
print(x)


# In[26]:


# Find length of the string
a = input("Enter the string: ")
print("Length = ",len(a))


# # Tuple Exercises:

# In[27]:


# Size of the Tuple
a = (1,2,3,4,5,6)
b = a.__sizeof__()
print(b)


# In[1]:


# Max & Min elements in Tuple
a = (1,2,3,4,5)
x = max(a)
y = min(a)
print("The Maximum element is ",x)
print("The Minimum element is ",y)


# In[123]:


# Sum of Tuple Elements
a = (1,2,3,4,5)
x = sum(a)
print("The Sum of the Tuple is",x)


# # Dictionary Exercises:

# In[63]:


# Sort Dictionaries by Key or Value
a = {"key1":"a","key3":"b","key2":"c","key5":"d","key4":"e"}
print(sorted(a))


# In[6]:


# Dictionary with keys having multiple inputs
import random as rn
a = {}
x,y,z = 1,2,3
a[x,y,z] = "a";
x,y,z = 4,5,6
a[x,y,z] = "b";
print(a)


# # Set Exercises:

# In[4]:


# Maximum and Minimum in a Set
a = {1,2,3,4,5}
print(a)
print("Maximum =",max(a))
print("Minimum =",min(a))


# In[6]:


# Size of a set
a = {1,2,3,4,5,6}
b = a.__sizeof__()
print(b)


# # Matrix Exercises:

# In[10]:


# Assigning Subsequent Rows to Matrix first row elements
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print("The Original list : ",str(a))
b = {a[0][e] :  a[e + 1] for e in range(len(a) - 1)}
print("The Assigned Matrix : ", str(b))


# In[18]:


# Adding and Subtracting Matrices in Python
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 5], [6, 7]])
print("A matrix:")
print(A)
print("B matrix:")
print(B)
print("Sum matrix:")
print(np.add(A, B))
print("Difference Matrix:")
print(np.subtract(A,B))


# # Functions Exercises:

# In[20]:


# Get multiple arguments using function
def greeting(name,nickname):
    print("Happy Birthday {} {} ".format(name,nickname))
greeting("Arun","Kutty")


# In[9]:


# Get list of parameters name from a function 
def fun(a, b):
    return a**b 
import inspect  
print(inspect.signature(fun)) 

