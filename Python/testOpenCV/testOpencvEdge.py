import sys
import cv2
import numpy as np 
import matplotlib.pyplot as plt


def show_img(image):
	plt.imshow(image)
	plt.axis("off")
	plt.show()

def RobertsOperator(roi):
	operator_first = np.array( [[-1,0], [0,1]] )
	operator_second = np.array( [[0,-1], [1,0]] )
	return np.abs(np.sum(roi[1:,1:]*operator_first)) + np.abs(np.sum(roi[1:,1:]*operator_second))

def RobertsAlogrithm(image):
	image = cv2.copyMakeBorder(image, 1,1,1,1, cv2.BORDER_DEFAULT)
	for i in range(1, image.shape[0]):
		for j in range(1, image.shape[1]):
			image[i,j] = RobertsOperator(image[i-1:i+2, j-1:j+2])
	return image[1:image.shape[0], 1:image.shape[1]]


def SobelOperator(roi, operator_type):
	if operator_type =="horizontal":
		sobel_operator = np.array( [ [-1,-2,-1], [0,0,0], [1,2,1] ] )
	elif operator_type == "vertical":
		sobel_operator = np.array( [ [-1,0,1], [-2,0,2], [-1,0,1] ] )
	else:
		raise("type Error")
	result = np.abs(np.sum(roi*sobel_operator))
	return result

def SobelAlogrithm(image, operator_type):
	new_image = np.zeros(image.shape)
	image = cv2.copyMakeBorder(image, 1,1,1,1, cv2.BORDER_DEFAULT)
	for i in range(1, image.shape[0]-1):
		for j in range(1, image.shape[1]-1):
			new_image[i-1, j-1] = SobelOperator(image[i-1:i+2, j-1:j+2], operator_type)
	new_image = new_image*(255/np.max(image))
	return new_image.astype(np.uint8)



def main():

	kodim09 = cv2.imread('/home/wanglei/images/Kodak_png/kodim09.png')
	kodim = cv2.cvtColor(kodim09, cv2.COLOR_BGR2RGB)
	show_img(kodim)
	print "type of kodim is ", type(kodim)
	print '\n'
	print "shape of kodim is ", kodim.shape
	print '\n' 

	kodim_gray = cv2.cvtColor(kodim, cv2.COLOR_RGB2GRAY)
	kodim_gray = cv2.resize(kodim_gray, (200, 200))



	Robert_kodim = RobertsAlogrithm(kodim_gray)
	plt.imshow(Robert_kodim, cmap="binary")	
	plt.axis("off")
	plt.show()



	plt.subplot(121)
	plt.title("horizontal")
	plt.imshow(SobelAlogrithm(kodim_gray,"horizontal"), cmap="binary")
	plt.axis("off")
	plt.subplot(122)
	plt.title("vertical")
	plt.imshow(SobelAlogrithm(kodim_gray,"vertical"), cmap="binary")
	plt.axis("off")
	plt.savefig('kodim_sobel.jpg')
	plt.show()

if __name__ == "__main__":
	main()