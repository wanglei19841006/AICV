import sys
import numpy as np 

class MyClass:
	i = 123
	def f(self):
		return 'Hello world'
print MyClass.i 

MyClass.i = 10
print MyClass.i 

x = MyClass()
print x.i 
x.f()
xf = x.f
xf()
MyClass.f(x)
print '\n'



print "=============class Complex================"
class Complex:
	def __init__(self, realpart, imagepart):
		self.r = realpart
		self.i = imagepart

x = Complex(3.1, -4.5)
print x.r, x.i 
print '\n' 

print "=============function not in class================"
def f1(self, x, y):
	return min(x, x+y)

class C:
	f = f1
	def g(self):
		return 'how long will I love you'
	h = g
p = C()
print "f = ", p.f(3, 6)
print '\n'
print p.h()
print '\n' 


print "=============class Bag================"
class Bag:
	"""docstring for Bag"""
	def __init__(self):
		self.data = [3.14159]
	def add(self, x):
		self.data.append(x)
	def addtwice(self, x):
		self.add(x)
		self.add(x)

b = Bag()
print b.data
b.add('999')
print b.data
b.addtwice('good')
print b.data
print '\n' 


print "================Derive Class============"
class Mapping:
	def __init__(self, iterable):
		self.items_list = []
		self.__update(iterable)

	def update(self, iterable):
		for item in iterable:
			self.items_list.append(item) 
	__update = update

class MappingSubclass(Mapping):
	def update(self, keys, values):
		for item in zip(keys, values):
			self.items_list.append(item)
		
mapx = Mapping(range(10))
print mapx.items_list		
print '\n'

mapxx = MappingSubclass(range(3))
print mapxx.items_list
print '\n'

mapxx.update('goodmorning', range(10))
print mapxx.items_list
print '\n' 
