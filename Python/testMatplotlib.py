import sys
import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0, 2*np.pi, 50)
plt.plot(x, np.sin(x), 'r-o',
	     x, np.cos(x), 'g--')
plt.show()


plt.subplot(2,1,1)
plt.plot(x, np.sin(x), 'r-.')
plt.subplot(2,1,2)
plt.plot(x, np.cos(x), 'm-^')
plt.show()


plt.scatter(x, np.sin(x))
plt.show()

del x

x = np.random.rand(1000)
y = np.random.rand(1000)
size = np.random.rand(1000)*50
colour = np.random.rand(1000)
plt.scatter(x,y,size,colour)
plt.colorbar()
plt.show()

del x, y, size, colour

x = np.random.randn(1000)
plt.hist(x, 50)
plt.show()

del x 

x = np.linspace(0, 2*np.pi, 50)
plt.plot(x, np.sin(x), 'r-x', label='Sin(x)')
plt.plot(x, np.cos(x), 'g-^', label='Cos(x)')
plt.legend()
plt.xlabel('Rads')
plt.ylabel('Amplitude')
plt.title('Sin and Cos Waves')
plt.show()
del x
