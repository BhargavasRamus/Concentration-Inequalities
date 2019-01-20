import numpy as np 
import matplotlib.pyplot as plt 
import IPython.core.pylabtools import figsize
import pandas as pd 
import scipy as sp 

n = 1000
results = []
for n in range(1,10000):
	throws = np.random.randint(1,7,n)
	mean_throws = throws.mean()
	results.append(mean_throws)

df = pd.DataFrame({'throws':results})

figsize(11,9)
df.plot(title='LLN (Guassian)',color='r')
plt.xlabel("N")
plt.ylabel("Average")
