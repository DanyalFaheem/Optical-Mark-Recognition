# References
# 1- Code provided by Dr. Akhtar Jamil
# 2- https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_properties/py_contour_properties.html

import cv2
import numpy as np
import matplotlib.pyplot as plt

# TODO: Reading Image
path = r'C:\Users\USER\Desktop\Digital Image Processing\Assignment#3\data\img3.png' 
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# TODO: Smoothing the image 
img=cv2.GaussianBlur(img,(3,3),1,0)
# TODO: Applying threshold on the image (the threshold value was generated on hit and run basis)
threshold, bw = cv2.threshold(img, 148, 255, cv2.THRESH_BINARY)  
# TODO: Finding Contours
contours, hierarchy = cv2.findContours(bw,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# TODO : Reading the image again in coloured mode
img_color = cv2.imread(path,cv2.IMREAD_COLOR)
# TODO : Drawing Bounding rectangle on first and last contour to cover the whole zebra crossing
x,y,w,h = cv2.boundingRect(contours[0])   # bounding rectangle on first contour
x2,y2,w2,h2 = cv2.boundingRect(contours[len(contours)-1])    # bounding rectangle on last contour
cv2.rectangle(img_color,(x,y),(x2+w2,y2+h2),(0,0,255),3)   # drawing rectangle

# TODO: Displaying the number of white strips
font = cv2.FONT_HERSHEY_COMPLEX
place = ((int)(50),(int)(50))
cv2.putText(img_color, "White strips : "+str(len(contours)) ,place, font , 1, (0,255,0), 1, cv2.LINE_AA)

# TODO: plotting the image
plt.imshow(img_color)
plt.axis('off')
plt.show()