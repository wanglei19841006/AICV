import numpy as np 
import matplotlib.pyplot as plt 

mu, sigma = 0, 0.1
s = np.random.normal(loc=mu, scale=sigma, size = 100)
print('s', s)

count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 
	1/(sigma * np.sqrt(2*np.pi)) * np.exp( -(bins-mu)**2 / (2*sigma**2)), 
	linewidth=2, 
	color='green')
plt.show()