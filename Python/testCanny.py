import sys
import cv2
import numpy as np 
import matplotlib.pyplot as plt 
# import testOpencvEdge
from testOpencvEdge import SobelOperator
from testOpencvEdge import SobelAlogrithm



def img_show(image):
	plt.imshow(image)
	plt.axis("off")
	plt.show()

def gray_img_show(image):
	plt.imshow(image, cmap="gray")
	plt.axis("off")
	plt.show()

def GaussianOperator(roi):
	GaussianKernel = np.array( [ [1,2,1], [2,4,2], [1,2,1] ] )
	result = np.sum(roi*GaussianKernel/16)
	return result

def GaussianSmooth(image):
	new_image = np.zeros(image.shape)
	image = cv2.copyMakeBorder(image, 1,1,1,1, cv2.BORDER_DEFAULT)
	for i in range(1, image.shape[0]-1):
		for j in range(1, image.shape[1]-1):
			new_image[i-1, j-1] = GaussianOperator( image[i-1:i+2, j-1:j+2] )
	return new_image.astype(np.uint8)

def NonmaximumSuppression(image, cita):
	keep = np.zeros(cita.shape)
	cita = np.abs(cv2.copyMakeBorder(cita, 1,1,1,1, cv2.BORDER_DEFAULT))
	for i in range(1, cita.shape[0]-1):
		for j in range(1, cita.shape[1]-1):
			if cita[i][j]>cita[i-1][j] and cita[i][j]>cita[i+1][j]:
				keep[i-1][j-1] = 1
			elif cita[i][j]>cita[i][j+1] and cita[i][j]>cita[i][j-1]:
				keep[i-1][j-1]=1
			elif cita[i][j]>cita[i+1][j+1] and cita[i][j]>cita[i-1][j-1]:
				keep[i-1][j-1]=1
			elif cita[i][j]>cita[i-1][j+1] and cita[i][j]>cita[i+1][j-1]:
				keep[i-1][j-1]=1
			else:
				keep[i-1][j-1] = 0
	return keep*image


def CannyAlogrithm(image, MINThreshold, MAXThreshold):
	image = GaussianSmooth(image)
	Gx = SobelAlogrithm(image, "horizontal")
	Gy = SobelAlogrithm(image, "vertical")
	# print "Gx = ", Gx 
	# print '\n'
	# print "Gy = ", Gy 
	# print '\n' 

	G = np.sqrt( np.square(Gx.astype(np.float64)) + np.square(Gy.astype(np.float64)) )
	# print "G = ", G
	# print '\n'

	#G = G*(255/np.max(G)).astype(np.uint8)
	cita = np.arctan2(Gy.astype(np.float64), Gx.astype(np.float64))
	# print "cita = ", cita 
	# print '\n'

	nms_image = NonmaximumSuppression(G, cita)
	print "max of nms_image is ", np.max(nms_image)
	print '\n'
	
	nms_image = (nms_image*(255/np.max(nms_image))).astype(np.uint8)
	usemap = np.zeros(nms_image.shape)
	high_list = []
	for i in range(nms_image.shape[0]):
		for j in range(nms_image.shape[1]):
			if nms_image[i,j]>MAXThreshold:
				high_list.append( (i,j) )

	direct = [ (0,1), (1,1), (-1,1), (-1,-1), (1,-1), (1,0), (-1,0), (0,-1)]
	def DFS(stepmap, start):
	    route = [start]
	    while route:
	    	now = route.pop()
	    	if usemap[now] == 1:
	    		break
	    	usemap[now] = 1
	    	for dic in direct:
	    		next_coodinate = (now[0] + dic[0], now[1]+dic[1])
	    		if next_coodinate[0]<stepmap.shape[0]-1 and next_coodinate[0]>=0 \
	    		and next_coodinate[1]<stepmap.shape[1]-1 and next_coodinate[1]>=0 \
	    		and not usemap[next_coodinate] and nms_image[next_coodinate]>MINThreshold:
	    		    route.append(next_coodinate)
	
	for i in high_list:
		DFS(nms_image, i)
	return nms_image*usemap
	    




def main():

	kodim = cv2.imread('/home/wanglei/images/Kodak_png/kodim20.png')
	kodim = cv2.cvtColor(kodim, cv2.COLOR_BGR2RGB)
	img_show(kodim)
	kodim_gray = cv2.cvtColor(kodim, cv2.COLOR_RGB2GRAY)



	kodim_smooth = GaussianSmooth(kodim_gray)
	plt.subplot(121)
	plt.title("origin image")
	plt.axis("off")
	plt.imshow(kodim_gray, cmap="gray")

	plt.subplot(122)
	plt.title("GaussianSmooth image")
	plt.axis("off")
	plt.imshow(kodim_smooth, cmap="gray")
	plt.show()

	Gx = SobelAlogrithm(kodim_smooth, "horizontal")
	Gy = SobelAlogrithm(kodim_smooth, "vertical")
	# print "Gx = ", Gx 
	# print '\n'
	# print "Gy = ", Gy 
	# print '\n' 

	G = np.sqrt(np.square(Gx.astype(np.float64)) + np.square(Gy.astype(np.float64)))
	cita = np.arctan2(Gy.astype(np.float64), Gx.astype(np.float64))
	# print "G = ", G
	# print '\n' 
	# print "cita = ", cita 
	# print '\n'

	plt.imshow(G.astype(np.uint8), cmap="gray")
	plt.axis("off")
	plt.show()


	
	nms_image = NonmaximumSuppression(G, cita)
	print "max of nms_image is ", np.max(nms_image)
	print '\n'
	nms_image = (nms_image*(255/np.max(nms_image))).astype(np.uint8)

	plt.imshow(nms_image, cmap="gray")
	plt.axis("off")
	plt.show()


	MAXThreshold = np.max(nms_image)/4*3
	MINThreshold = np.max(nms_image)/4
	usemap = np.zeros(nms_image.shape)
	high_list = []

	for i in range(nms_image.shape[0]):
	    for j in range(nms_image.shape[1]):
	        if nms_image[i,j]>MAXThreshold:
	            high_list.append((i,j))

	direct =[ (0,1), (1,1), (-1,1), (-1,-1), (1,-1), (1,0), (-1,0), (0,-1) ]
	def DFS(stepmap, start):
		route = [start]
		while route:
			now = route.pop()
			if usemap[now] ==1:
				break
			usemap[now]=1
			for dic in direct:
				next_coodinate = (now[0]+dic[0], now[1]+dic[1])
				if not usemap[next_coodinate] and nms_image[next_coodinate]>MINThreshold \
				and next_coodinate[0]<stepmap.shape[0]-1 and next_coodinate[0]>=0 \
				and next_coodinate[1]<stepmap.shape[1]-1 and next_coodinate[1]>=0:
				   route.append(next_coodinate)	
	for i in high_list:
		DFS(nms_image, i)
	plt.imshow(nms_image*usemap, cmap="gray")
	plt.axis("off")
	plt.show()



	kodim_canny = CannyAlogrithm(kodim_gray, MINThreshold, MAXThreshold)
	gray_img_show(kodim_canny)

if __name__ == '__main__':
	main()
