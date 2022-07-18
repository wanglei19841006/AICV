#-*- coding: utf-8
#from pylab import *
#mpl.rcParams['font.sans-serif']=['SimHei']
#mpl.rcParams['axes.unicode_minus']=False

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import sys

a = np.random.rand(12)
b = np.reshape(a,[3,4])
print "a = ", a
print '\n'
print "b = ", b 
print '\n'



# plt.figure(1)
# t=np.linspace(0,20,100)
# y=np.sin(t)
# plt.plot(t,y)
# plt.ylabel('some numbers')
# plt.savefig('/home/wanglei/images/temp/sin.jpg')
# plt.show()

# f=open('/home/wanglei/Program/Python/test_results2.txt','w+')
# ##print t
# for i in range(0,len(t)):
#   f.write(str(t[i])+"\t")
# f.close()

##name =['wang','li','zhao']
##address=['shenzhen','beijing','shanghai']
##f = open("E:\\Program\\Python\\test_results1.txt", "w+")
##f.write("name\t address\n")
##for i in range(0, len(name)):
##    f.write(name[i] + "\t" + address[i] + "\n")
##f.close()
