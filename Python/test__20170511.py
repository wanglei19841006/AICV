# -*- coding: utf-8 -*-
"""
Created on Thu May 11 09:30:35 2017

@author: siat39--wanglei
"""

import matplotlib.pyplot as plt
#import math
import numpy as np
import datetime


#import os
#t=os.system('$(date +%Y-%m-%d_%H:%M:%S)')
#print t

import commands
dir(commands)
commands.getoutput("date")

a = dir(np)
b=100000
c='Hello World!'
str1=r'this \f?ff'
print str1
template='%.2f %s haha $%d'
print template
str1=template % (4.88, 'hola', 2)
print str1
#print a
print 'the type of a is', type(a),'list Module Contents'

print 'the type of b is', type(b)
print 'the type of c is', type(c)

dat1=datetime.datetime.now()
dat2=datetime.datetime.now().date()
#dat3=datetime.time.tzname()
print dat1
print dat2
#print dat3
tup1=range(16)
print tup1,type(tup1)

tup2=np.array(tup1)
print tup2,type(tup2)
tt2=tup2.reshape(2,8)
print tt2
tt3=tup2.reshape(2,4,2)
print tt3

dict1={'star':'earth', 2:[177,68], 'school':'Xidian', 'year':2010,'degree':'Ph.D'}
print dict1.keys()
print dict1['star']
print dict1[2]
print dict1['degree']

def printScreen(str):
    print str
    return
printScreen("The first function...")    
printScreen("Hello, world!")    
       
def sinfunction(a,colore):
    t=np.linspace(0,np.pi,100)
    y=np.sin(a*t)
    x=np.argmax(y)
    print 'x= ', x
    plt.plot(t,y,colore, label=u'y=sin(x)')
    plt.title(u'sin')
    plt.legend()
    plt.xlabel(u"x")
    plt.ylabel(u"sin(x)")
    print 'the type of t is', type(t)
    print 'the type of y is', type(y)
    return
plt.figure(1),sinfunction(1,'b')
plt.grid(True)
plt.figure(2),sinfunction(5,'m')
    
print 421000000/6342    