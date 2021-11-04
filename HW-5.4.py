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


def romberg_core(f,a,b,tol)


#define an iteration variable
i = 0

#define the maximum number of iteration
imax = 1000000

#define an error estimate, set to a large value:
delta = 100.0*np.fabs(tols)

#set an array of integral answers
I = np.zeros(imax.dtype=float)

 while(delta>tol):
        while we have reached the maximum iterations
        if(i>imax):
            print("Max iteration reached.")
            raise StopIteration ('Stop iteration after after ',i)
            
#Return the answer
return I[i]

