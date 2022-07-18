#import sys
import numpy as np 
#import matplotlib.pyplot as plt

# a = np.linspace(0, 2*np.pi, 50)
# b = np.sin(a)
# plt.plot(a,b)
# mask = b>=0
# plt.plot(a[mask], b[mask], 'bo')
# mask = (b>=0)&(a<=np.pi/2)
# plt.plot(a[mask], b[mask], 'go')
# plt.show()

a = np.arange(0, 100, 10)
b = a[:5]
c = a[a>=50]
print (a, '\n')
print (b, '\n')
print (c, '\n')
d = np.where(a<50)
e = np.where(a>=50)[0]
print ("where a<50____", d, '\n')
print ("where a>=50____", e, '\n')
