import numpy as np 
import cv2
import sys
import matplotlib.pyplot as plt 


def img_show(image):
	plt.imshow(image)
	plt.axis("off")
	plt.show()




kodim = cv2.imread('/home/wanglei/images/Kodak_png/kodim19.png')
kodim = cv2.cvtColor(kodim, cv2.COLOR_BGR2RGB)
print "shape of kodim is ", kodim.shape
print '\n'
img_show(kodim)

kodim_gray = cv2.cvtColor(kodim, cv2.COLOR_RGB2GRAY)


def LaplaceOperator(roi, operator_type):
	if operator_type == "fourfields":
		laplace_operator = np.array( [ [0,1,0], [1,-4,1], [0,1,0] ] )
	elif operator_type == "eightfields":
		laplace_operator = np.array( [ [1,1,1], [1,-8,1], [1,1,1] ] ) 
	else:
		raise("type Error")
	result = np.abs(np.sum(roi*laplace_operator))
	return result

def LaplaceAlogrithm(image, operator_type):
	new_image = np.zeros(image.shape)
	image = cv2.copyMakeBorder(image, 1,1,1,1, cv2.BORDER_DEFAULT)
	for i in range(1, image.shape[0]-1):
		for j in range(1, image.shape[1]-1):
			new_image[i-1, j-1] = LaplaceOperator(image[i-1:i+2, j-1:j+2], operator_type)
	new_image = new_image*(255/np.max(image))
	return new_image.astype(np.uint8)

plt.subplot(121)
plt.title("fourfields")
plt.imshow(LaplaceAlogrithm(kodim_gray, "fourfields"), cmap="binary")
plt.axis("off")

plt.subplot(122)
plt.title("eightfields")
plt.imshow(LaplaceAlogrithm(kodim_gray, "eightfields"), cmap="binary")
plt.axis("off")
plt.savefig('kodim19_laplace.jpg')
plt.show()
