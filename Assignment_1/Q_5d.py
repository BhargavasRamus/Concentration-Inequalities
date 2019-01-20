import numpy as np
import matplotlib.pyplot as plt

n = 1000
N = 100
u = 0.5
v = 1

X = np.linspace(0,1,218)
x1 = np.zeros((n))
x2 = np.zeros((n))
x3 = np.zeros((n))
x4 = np.zeros((n))

#guassian distribution
for i in range(n):
	for j in range(N):
		x1[i] += np.random.randn()
	x1[i] *= 1/N

#uniform distribution
for i in range(n):
	for j in range(N):
		x2[i] += np.random.random()
	x2[i] *= 1/N

#exponential distribution
for i in range(n):
	for j in range(N):
		x3[i] += np.random.exponential(u)
	x3[i] *= 1/N

#binomial distribution
for i in range(n):
	for j in range(N):
		x4[i] += np.random.poisson()
	x4[i] *= 1/N

#CLT
#var = v/N
#guassian = (1/np.sqrt(2*np.pi*var))*np.exp(-(X-u)**2/(2*var))

plt.subplot(4, 1, 1)
plt.hist(x1,100,color='#348ABD',label="%d RVS"%(N))
plt.xlabel('x')
plt.xlim([0,1])
leg = plt.legend(loc="upper right")
leg.get_frame().set_alpha(0.1)

plt.subplot(4, 1, 2)
plt.hist(x2,100,color='#348ABD',label="%d RVS"%(N))
plt.xlabel('x')
plt.xlim([0,1])
leg = plt.legend(loc="upper right")
leg.get_frame().set_alpha(0.1)

plt.subplot(4, 1, 3)
plt.hist(x3,100,color='#348ABD',label="%d RVS"%(N))
plt.xlabel('x')
plt.xlim([0,1])
leg = plt.legend(loc="upper right")
leg.get_frame().set_alpha(0.1)

plt.subplot(4, 1, 4)
plt.hist(x4,100,color='#348ABD',label="%d RVS"%(N))
plt.xlabel('x')
plt.xlim([0,1])
leg = plt.legend(loc="upper right")
leg.get_frame().set_alpha(0.1)

plt.show()
