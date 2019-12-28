import cv2
from keras.models import load_model
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
import numpy as np
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils

def Binarization(img):
	threshold = 230
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
	img=255-img
	return img

def get_Prediction(img):
	model=load_model('cnn_model.h5')
	cv2.imshow("Binarized_image",img)
	cv2.waitKey(0)
	img = np.reshape(img,[1,28,28,1])
	print(model.predict_classes(img )) 


img=cv2.imread('model_test_8.jpg') 
Resized_img=cv2.resize(img,(28,28))
print(Resized_img.shape)
cv2.imshow("img",Resized_img)
cv2.waitKey(0)   
Binarized_img=Binarization(Resized_img)
print(Binarized_img.shape)
get_Prediction(Binarized_img) 
