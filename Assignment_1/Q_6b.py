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
for n in range(1,10000):
	results1.append(np.random.randint(1,7,n).mean())

#uniform distribution
for n in range(1,10000):
	results2.append(np.random.random(1,7,n).mean())

#exponential distribution
for n in range(1,10000):
	results3.append(np.random.exponential(1,7,n).mean())

#poisson distribution
for n in range(1,10000):
	results4.append(np.random.poisson(1,7,n).mean())

plt.subplot(4,1,1)
df = pd.DataFrame({'throws':results1})
df.plot(title='LLN (Guassian)',color='r')
plt.xlabel("N")
plt.ylabel("Average")

plt.subplot(4,1,2)
df = pd.DataFrame({'throws':results2})
df.plot(title='LLN (uniform)',color='r')
plt.xlabel("N")
plt.ylabel("Average")

plt.subplot(4,1,3)
df = pd.DataFrame({'throws':results3})
df.plot(title='LLN (exponential)',color='r')
plt.xlabel("N")
plt.ylabel("Average")

plt.subplot(4,1,4)
df = pd.DataFrame({'throws':results4})
df.plot(title='LLN (poisson)',color='r')
plt.xlabel("N")
plt.ylabel("Average")

