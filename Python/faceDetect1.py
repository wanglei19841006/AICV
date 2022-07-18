# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 16:33:06 2016

@author: siat39
"""

# -*- coding: cp936 -*-

from PIL import Image 
import cv2

print abs(-123.6)

  
img = cv.LoadImage("friends.jpg");  
  
image_size = cv.GetSize(img)#获取图片的大小  
greyscale = cv.CreateImage(image_size, 8, 1)#建立一个相同大小的灰度图像  
cv.CvtColor(img, greyscale, cv.CV_BGR2GRAY)#将获取的彩色图像，转换成灰度图像  
storage = cv.CreateMemStorage(0)#创建一个内存空间，人脸检测是要利用，具体作用不清楚  
       
cv.EqualizeHist(greyscale, greyscale)#将灰度图像直方图均衡化，貌似可以使灰度图像信息量减少，加快检测速度  
# detect objects  
cascade = cv.Load('haarcascade_frontalface_alt2.xml')#加载Intel公司的训练库  
  
#检测图片中的人脸，并返回一个包含了人脸信息的对象faces  
faces = cv.HaarDetectObjects(greyscale, cascade, storage, 1.2, 2,  
                                     cv.CV_HAAR_DO_CANNY_PRUNING,  
                                     (50, 50))  
  
#获得人脸所在位置的数据  
j=0 #记录个数  
for (x,y,w,h),n in faces:  
    j+=1  
    cv.SetImageROI(img,(x,y,w,h))#获取头像的区域  
    cv.SaveImage("face"+str(j)+".jpg",img);#保存下来  
   