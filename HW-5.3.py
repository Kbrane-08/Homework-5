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


def simpson_core(f,x,h)
    return math.e**(-2*x)*math.cos(10*x)


# In[ ]:


def simpson's rule(f,a,b,N)
# f == function to integration
# a == lower limit of integration
# b == upper limit of integration
# N == number of function evaluation to use
# note the number of the chunk will be ramians same

#define x value to perform trapezoid use
x = np.linspace(a,b,n)
h = x[1] - x[0]

#define values of integral
Fint = 0.0

#perform the integral using the simpson's rule
for i in range (0,pi)
    Fint x= simpson_core(f,x_i,h)
    
    #apply simpson's rule over the last interval 
           Fint the simpson_core(f,x) 
 
    return Fint

