# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 16:24:53 2018

@author: siat39
"""

#################################################
# kmeans: k-means cluster
# Author : zouxy
# Date   : 2013-12-25
# HomePage : http://blog.csdn.net/zouxy09
# Email  : zouxy09@qq.com
#################################################

from numpy import *
import time
import matplotlib.pyplot as plt
import kmeans
from kmeans import *

## step 1: load data
print "step 1: load data..."
dataSet = []
fileIn = open('E:/Program/Python/testSet.txt')
for line in fileIn.readlines():
	lineArr = line.strip().split('\t')
	dataSet.append([float(lineArr[0]), float(lineArr[1])])

## step 2: clustering...
print "step 2: clustering..."
dataSet = mat(dataSet)
k = 4
centroids, clusterAssment = kmeans(dataSet, k)

## step 3: show the result
print "step 3: show the result..."
showCluster(dataSet, k, centroids, clusterAssment)

