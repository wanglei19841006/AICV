import numpy as np 

print('\n---------number---------\n')
i = 100
print(type(i))

f = 3.1415926
print(type(f))

c = 1+2j
print(c)
print(type(c))

print(isinstance(c, complex))

print('\n---------string---------\n')
s = 'hello, world!'
print(s)
s = "hello, python!"
print(s)
s = '''hello, sublime and
... world!'''
print(s)
print(s[4])
print(s[7:10])
print(s[-4:-1])


s1 = "come"
s2 = "on"
print(s1 + ' ' + s2)
print((s1+' '+s2)*3)

print('\n---------list---------\n')
list1 = [1, 5.5, 'Python', 108, 36, 99, 88, 121, 256]
print(type(list1))
print(list1[2])
print(list1[0:2])
print(list1[2:])
list1[2] = 'world'
print(list1)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])
print(list2[0:3])
print(list2[3:5])
print(list2[8])
print(list2[0:9])

print('\n---------tuple---------\n')
tuple1 = (36, 3.1415926, 2+3j, 'flower', [1, 2, 3])
print(type(tuple1))
print(tuple1[0])
print(tuple1[1])
print(tuple1[0:2])
print(tuple1[3])
print(tuple1[4])
tuple2 = (6,)
print(tuple2)


print('\n---------set---------\n')
set1 = {36, 'Python good', 3+6j}
print(type(set1))
print(set1)
if(36 in set1):
	print('36 is in set1')
else:
	print('36 is no in set1')

a = set('abcdefg')
b = set('abdghijk')
print(a)
print(b)
print(a - b)
print(b - a)
print(a | b)
print(a & b)
print(a ^ b)

print('\n---------Dictionary---------\n')
dic1 = {1:'china', 'USA':2}
print(dic1)
print(type(dic1))

dic1['name'] = 'Python'
dic1['website'] = 'www.python.org'
print(dic1)
print(dic1[1])
print(dic1['USA'])
print(dic1['name'])
print(dic1['website'])
print('')
