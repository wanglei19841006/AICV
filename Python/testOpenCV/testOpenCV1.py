import sys
import cv2
import matplotlib.pyplot as plt 
import numpy as np 
from PIL import Image 


def show_cv_img(cv_img):
	plt.imshow(cv_img)
	plt.axis("off")
	plt.show()


img0 = cv2.imread('/home/wanglei/images/Kodak_png/kodim23.png')
img1 = cv2.cvtColor(img0,cv2.COLOR_BGR2RGB)
print "type of img1 is ", type(img1)
print '\n' 
print "size of img1 is ", sys.getsizeof(img1)
print '\n' 
print "shape of img1 is ", img1.shape
print '\n' 
plt.figure(1)
show_cv_img(img1)
# plt.imshow(img1)
# plt.axis("off")
# plt.show()
print '\n' 


img2 = cv2.GaussianBlur(img1,(3,3),0)
plt.figure(2)
show_cv_img(img2)
cv2.imwrite('GaussianBlur_kodim.jpg', img2)



canny = cv2.Canny(img1, 50, 150)
plt.figure(3)
show_cv_img(canny)
cv2.imwrite('canny_kodim.jpg', canny)
# cv2.imshow('Canny',canny)
# cv2.waitkey(0)
# cv2.destroyAllWindows()

img1_gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
plt.figure(4)
show_cv_img(img1_gray)  # wrong show for gray image
cv2.imwrite('gray_kodim.jpg', img1_gray)

