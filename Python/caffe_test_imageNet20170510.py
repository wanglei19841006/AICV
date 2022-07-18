# -*- coding: utf-8 -*-
"""
Created on Wed May 10 07:19:54 2017

@author: siat39--wanglei
"""

from caffe import imagenet  
from matplotlib import pyplot  
# Set the right path to your model file, pretrained model  
# and the image you would like to classify.  
MODEL_FILE = 'examples/imagenet_deploy.prototxt'  
PRETRAINED = '/home/jiayq/Downloads/caffe_reference_imagenet_model’  
IMAGE_FILE = '/home/jiayq/lena.png'  
   
net = imagenet.ImageNetClassifier(MODEL_FILE, PRETRAINED)   
#预测  
prediction = net.predict(IMAGE_FILE）  
#绘制预测图像  
print 'prediction shape:', prediction.shape  
pyplot.plot(prediction)  
prediction shape: (1000,)  
[<matplotlib.lines.Line2D at 0x8faf4d0>] #结果如图所示  

