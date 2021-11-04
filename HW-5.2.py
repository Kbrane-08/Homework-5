#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('mathplotlib', 'inline')
import mathplotlib.pyplot as plt
import np as numpy


# In[ ]:


def function_to_integrate(x):
# e^(-2x)*cos(10x)
return math.e**(-2*x)*math.cos(10*x)


# In[ ]:


def trapazoid core(f,x,h)
    return math.e**(-2*x)*math.cos(10*x)


# In[1]:


def trapezoid method(f,a,b,N)
#f == function to integration
#a == lower limit of integration
#b == upper limit of integration
#N == number of function evaluation to use

#define x value to perform trapezoid use
x = np.linspace(a,b,n)
h = x[1] - x[0]

#define the value of the interval
Fint = 0.0

#perform the integral using the trapezoid method
for i in range (0,pi)
    Fint x= trapezoid_core(f,x_i,h)
    
    #return the answer
    return Fint


# In[ ]:




