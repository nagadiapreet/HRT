import cv2

def Binarization(img):
	threshold = 230
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img = cv2.GaussianBlur(img,(5,5),0)
	ret,th1 = cv2.threshold(img,threshold,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	return th1

img = cv2.imread('row_8_col_2.jpg')
img = Binarization(img)
# cv2.imshow('', img)
# cv2.waitKey(0)

rows,cols = img.shape[:]

cols_coordinates = []
flag = True
for j in range(0,cols):

	temp_sum = 0
	for i in range(0,rows):
		temp_sum += img[i][j]

	if temp_sum == 255*rows and flag:
		cols_coordinates.append(j)
		flag = False
	if temp_sum<255*rows:
		flag = True

x = cols_coordinates[0]
print(cols_coordinates)

for i in range(1,len(cols_coordinates)):
	w = cols_coordinates[i]
	crop_img = img[:,x:w]
	x = w
	cv2.imshow('',crop_img)
	cv2.waitKey(0)