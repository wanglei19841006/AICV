import numpy as np 
a=[[1,2,3,4], [5,6,7,8], [9,10,11,12]]
b=np.array(a)
print type(a)
print "a=", a
print type(b)
print "b=", b
print '\n'

print "length of a =", len(a)
print "length of b =", len(b)
print "size of b = ", b.size
print "shape of b = ", b.shape
print '\n'

c = np.mat(a)
print "type of c is ", type(c)
print "c = ", c
print '\n'

d = np.mat(b)
print "type of d is ", type(d)
print "d = ", d
print "length of d = ", len(d)
print  "size of d = ", d.size
print "shape of d = ", d.shape
print '\n'

print c*d.T 
print '\n'

e = np.random.rand(12)
print e
print '\n'
print np.shape(e)
print '\n' 

f = np.reshape(e,(3,4))
print f 
print '\n'

g = np.random.randint(0,30, size=[3,5])
print "g = \n", g
print '\n'