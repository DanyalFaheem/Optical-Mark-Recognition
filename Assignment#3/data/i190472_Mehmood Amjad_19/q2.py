# References
# 1- Code provided by Dr. Akhtar Jamil
# 2- https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_properties/py_contour_properties.html

import cv2
import numpy as np
import matplotlib.pyplot as plt

# TODO: Reading Image
path = r'C:\Users\USER\Desktop\Digital Image Processing\Assignment#3\data\img2.png' 
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# TODO: Getting negative of the image
img = 255 - img
# TODO: Finding Contours
contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# TODO : Getting the contour with the max area (highest number of frequency)
# declaring a list to store the areas
area = [] 
for i in range ( len(contours) ):
    # appending the area of each contours to the list
    area.append(cv2.contourArea(contours[i]))
#getting the max area from the list
area_max = max(area)
#getting the index of the max area from the list
area_max_index = area.index(area_max)

# TODO : Reading the image again in coloured mode
img_color = cv2.imread(path,cv2.IMREAD_COLOR)
# TODO : Drawing Bounding rectangle around the wave with highest frequency
temp = np.zeros_like(img_color)
x,y,w,h = cv2.boundingRect( contours[area_max_index] )  
cv2.rectangle(img_color,(x,y),(x+w,y+h),(0,255,0),3)   
# TODO: plotting the image
plt.imshow(img_color)
plt.axis('off')
plt.show()