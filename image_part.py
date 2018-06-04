#!/usr/bin/python3

import cv2
import time

image = input("which image you want to open     ")
print(image)
img=cv2.imread(image)

#to display the shape of the chooswn image
shap=img.shape
#print(shap)
#printing the actual size of the image
print("The actual size of the image is :",shap[0],",",shap[1])


a='''
Now what part of the image you want ??
1/2 part
1/3 part
1/4 part
'''
print(a)

#taking input from user
inp = input("choose one part you want   " )
print(inp)

#if input given by the user is 
if inp == '1/2':
	part = 2
elif inp == '1/3':
 	part = 3	
elif inp == '1/4':
	part = 3


width=int(shap[0]/part)
print("the width of the image is: ",width)
height=int(shap[1]/part)
print("the height of the image is :  ",height)

#to cut a part of the image
new_image = img[0:width,0:height]

#to display the rest of the width and height of the image
rem_width=int(shap[0]-width)
print(rem_width)
rem_height=int(shap[1]-height)
print(rem_height)

#to display the remaining image
rem_part_img=img[width:rem_width,height:rem_height]

#to show the desired part of the image
cv2.imshow('window',new_image)
time.sleep(1)

#to show the remaining part of the image
cv2.imshow('window1',rem_part_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

