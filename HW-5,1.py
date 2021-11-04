#!/usr/bin/env python
# coding: utf-8

# In[22]:


# import the required libraries
import math
from scipy.integrate import quad


# In[3]:


# define the function to be integrated
def function_to_integrate(x): 
    # e^(-2x)*cos(10x)    
    return math.e**(-2*x)*math.cos(10*x)

# def the lower and upper bound of integration
#0 is the lower bound
#pi is the upper bound
#quad is the function_to_integrate, lower_bound, upper_bound


# In[24]:


result is the quad  # compute the result of the integration
print("Integrating e^(-2x)*cos(10x) from 0 to pi results:", result[0],"with error=",result[1])  # print the results


# In[ ]:




