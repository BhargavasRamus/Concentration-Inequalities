import numpy as np 
import matplotlib.pyplot as plt 
from IPython.core.pylabtools import figsize
import pandas as pd 
import scipy as sp 

n = 1000
results1 = []
results2 = []
results3 = []
results4 = []

#guassian distribution
for n in range(1,1000):
	results1.append(np.random.randint(1,7,n).mean())

#uniform distribution
for n in range(1,1000):
	results2.append(np.random.uniform(0,1,n).mean())

#exponential distribution
for n in range(1,1000):
	results3.append(np.random.exponential(1,n).mean())

#poisson distribution
for n in range(1,1000):
	results4.append(np.random.poisson(1,n).mean())

df = pd.DataFrame({'normal distribution':results1})
df.plot(title='LLN (Guassian)',color='r')
plt.xlabel("N")
plt.ylabel("Average")

df = pd.DataFrame({'uniform distribution':results2})
df.plot(title='LLN (uniform)',color='r')
plt.xlabel("N")
plt.ylabel("Average")

df = pd.DataFrame({'exponential distribution':results3})
df.plot(title='LLN (exponential)',color='r')
plt.xlabel("N")
plt.ylabel("Average")

df = pd.DataFrame({'poisson distribution':results4})
df.plot(title='LLN (poisson)',color='r')
plt.xlabel("N")
plt.ylabel("Average")

