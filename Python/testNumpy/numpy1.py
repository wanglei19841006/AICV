import numpy as np 

a = np.arange(9).reshape(3, 3)
b = a*2
print(a)
print(b)

print(np.hstack((a,b)))

print(np.vstack((a,b)))

print(np.dstack((a,b)))

print(np.column_stack((a,b)))

print(np.row_stack((a,b)))

print(np.hsplit(a, 3))
print('')
print(np.vsplit(a, 3))
print('')

c = np.arange(27).reshape(3,3,3)
print(np.dsplit(c, 3))
print('')

d = [i for i in range(0, 5)]
print(d)
print('')
d = np.array(a)
print(d)
print('')
print('shape of array             =', np.shape(d))
print('data type                  =', d.dtype)
print('dimension of array         =', np.ndim(d))
print('number of elements         =', np.size(d))
print('bytes of element in array  =', d.itemsize)
print('storage space of array is  =', d.nbytes)
print('')

e = [i for i in range(0, 5, 2)]
print(e)

print(np.arange(3))
print(np.arange(3.0))
print(np.arange(3, 8))
print(np.arange(3,8,2))
print(np.arange(0, 1, 0.1))
print(np.arange(0, 2, 0.2))
print('')

