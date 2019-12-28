import cv2
import PreProcessing
from keras.models import load_model
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
import numpy as np
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils

def removeBlackPixels():
	img = cv2.imread("Cropped_Images/row_11_col_1.png")
	cv2.imshow('', img)
	cv2.waitKey(0)
	# img = PreProcessing.Binarization(img)

	rows,cols = img.shape[:2]

	for i in range(rows-1):
		for j in range(cols-1):
			B = img[i][j][0]
			G = img[i][j][1]
			R = img[i][j][2]
			if (R<130 and G<130 and B<130):
				img[i][j] = [255,255,255]
			else:	
				print(R,G,B)

	cv2.imshow('', img)
	cv2.waitKey(0)
	return img

def FindBoundary(crop_img):
	rows, cols = crop_img.shape[:]

	x=0
	w=0
	h=0
	y=0
	flag=False

	vertical_sum=[]
	horizontal_sum=[]
	for j in range(cols):
		temp_sum = 0
		for i in range(rows):
			temp_sum += crop_img[i,j]
		vertical_sum.append(temp_sum)

	for i in range(rows):
		temp_sum = 0
		for j in range(cols):
			temp_sum += crop_img[i,j]
		horizontal_sum.append(temp_sum)

	temp = 255*rows
	for i in range(len(vertical_sum)):
		if vertical_sum[i]!=temp:
			x=i
			break

	for i in range(len(vertical_sum)-1,-1,-1):
		if vertical_sum[i]!=temp:
			w = i
			break

	temp = 255*cols
	for i in range(len(horizontal_sum)):
		if horizontal_sum[i]!=temp:
			y=i
			break

	for i in range(len(horizontal_sum)-1,-1,-1):
		if horizontal_sum[i]!=temp:
			h = i
			break

	# print(vertical_sum)
	# print(horizontal_sum)
	# print(rows,cols)
	# print(x,w)

	return crop_img[y:h,x:w]


def get_Prediction(img):
	# cv2.imshow("Binarized_image",img)
	# cv2.waitKey(0)
	img = np.reshape(img,[1,28,28,1])
	y_pred1=model.predict(img)
	print(np.argmax(y_pred1,axis=1))
	#print(model.predict(img )) 

def GetDigits(img):
	img = PreProcessing.Binarization(img)
	cv2.imshow('', img)
	# cv2.waitKey(0)

	rows,cols = img.shape[:]

	cols_coordinates = []
	flag = True
	for j in range(0,cols):

		temp_sum = 0
		for i in range(0,rows):
			temp_sum += img[i][j]

		if temp_sum == 255*rows and flag:
			cols_coordinates.append(j+5)
			flag = False
		if temp_sum<255*rows:
			flag = True

	print(cols_coordinates)
	x = cols_coordinates[0]

	for i in range(1,len(cols_coordinates)):
		w = cols_coordinates[i]
		crop_img = img[:,x:w]
		x = w
		# cv2.imshow('',crop_img)
		# cv2.waitKey(0)
		# cv2.imshow("Cropped_Image",crop_img)
		# cv2.waitKey(0)
		crop_img = FindBoundary(crop_img)
		crop_img = cv2.resize(crop_img, (20,20))

		temp_crop_img = []
		for i in range(28):
			temp = []
			for j in range(28):
				temp.append(0)
			temp_crop_img.append(temp)

		for i in range(20):
			for j in range(20):
				if crop_img[i][j]>127:
					crop_img[i][j] = 255
				else:
					crop_img[i][j] = 0

				if crop_img[i][j]==0:
					temp_crop_img[4+i][4+j] = 255

		# print(temp_crop_img)
		cv2.imshow('Boundary', np.float32(temp_crop_img))
		cv2.waitKey(0)
		#Resized_img=cv2.resize(crop_img,(28,28))
		# Resized_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
		#Resized_img=PreProcessing.smoothening(Resized_img)
		# cv2.imshow('crop_img', Resized_img)
		# cv2.waitKey(0)
		
		# Resized_img = 255-Resized_img
		# Resized_img=cv2.resize(Resized_img,(28,28)) 
		# kernel=np.ones((1,1),np.uint8)
		# Resized_img=cv2.dilate(Resized_img,kernel,iterations=20)
		get_Prediction(temp_crop_img)

#Loading Model
model=load_model('cnn_model.h5')

#img = removeBlackPixels()
img = cv2.imread('Cropped_Images/row_8_col_1.png')
GetDigits(img)