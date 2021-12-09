# References
# 1- Code provided by Dr. Akhtar Jamil with lecture 11
# 2- https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html
# 3- https://www.geeksforgeeks.org/python-opencv-cv2-line-method/
# 4- https://www.mathsisfun.com/algebra/trig-solving-sss-triangles.html
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
# TODO: Reading Image
path = r'C:\Users\USER\Desktop\Digital Image Processing\Assignment#3\data\img1.png' 
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# TODO: Finding Contours
contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# TODO: Reading the image again in coloured mode
img_color = cv2.imread(path,cv2.IMREAD_COLOR)

# TODO: Declaring lists to store the x and y coordinates of the center
arrX = []
arrY = []
# TODO: Drawing the centers of the circle (code provided by dr Akhtar Jamil)
for i in range(len(contours)):
    #getting the average of intensities between 2 pixels
    M = cv2.moments(contours[i])
    x = int(M["m10"] / M["m00"])
    y = int(M["m01"] / M["m00"])
    arrX.append(x)
    arrY.append(y)
    cv2.circle(img_color, (x, y), 5, (0, 255, 0), -1)
# TODO: Declaring list to store the distances, angles and gradients 
dist = []
angles = []
# TODO: Drawing lines and Calculating distances between the centers
for i in range (len(contours)):
    # inititalizing the startpoint for the line
    startpoint = (arrX[i],arrY[i])
    # initializing the endpoint for the line
    if (i == len(contours)-1):
        endpoint = (arrX[0],arrY[0])
    else: 
        endpoint = (arrX[i+1],arrY[i+1])
    # TODO: drawing a line between the circles    
    img_color = cv2.line(img_color, startpoint , endpoint , (255,0,0) , 3)
    # TODO: getting the distance between two centers
    if (i == len(contours)-1):
        Xcord = (arrX[0]-arrX[i])
        Ycord = (arrY[0]-arrY[i])
    else: 
        Xcord = (arrX[i+1]-arrX[i])
        Ycord = (arrY[i+1]-arrY[i])
    # Calculating distance between the centers using foromula : dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    dist.append( round(math.sqrt(Xcord**2 + Ycord**2),0) )

# TODO: Getting angles using the laws of cosine
# acos() function gives the cos inverse in radians      
# we use degrees() function to convert the radians into degrees then round it off     
# Let a, b and c be the 3 sides (our 3 distances at index 1,0,2 respectively)
# cos A = (b2 + c2 − a2) / 2bc
ang = round(math.degrees(math.acos( (dist[0]**2 + dist[2]**2 - dist[1]**2) / (2*dist[2]*dist[0]) ) ),0)
angles.append( ang )
# cos B = (c2 + a2 − b2)/2ca
ang = round(math.degrees(math.acos( (dist[2]**2 + dist[1]**2 - dist[0]**2) / (2*dist[2]*dist[1]) ) ),0)
angles.append( ang )
# C = 180 - A - B
ang = 180 - angles[0] - angles[1]
angles.append( ang )

# TODO: displaying the distances on image
font = cv2.FONT_HERSHEY_PLAIN
place = ((int)(arrX[0]+35),(int)(arrY[0]+20))
cv2.putText(img_color, str(dist[0]) ,place, font , 1, (255,255,255), 1, cv2.LINE_AA)
place = ((int)(arrX[1]-35),(int)(arrY[1]-80))
cv2.putText(img_color, str(dist[1]) ,place, font , 1, (255,255,255), 1, cv2.LINE_AA)
place = ((int)(arrX[2]-70),(int)(arrY[2]+80))
cv2.putText(img_color, str(dist[2]) ,place, font , 1, (255,255,255), 1, cv2.LINE_AA)

# TODO: displaying the agles on image
font = cv2.FONT_HERSHEY_PLAIN
place = ((int)(arrX[0]+8),(int)(arrY[0]-10))
cv2.putText(img_color, str(angles[0]) ,place, font , 1, (0,0,255), 1, cv2.LINE_AA)
place = ((int)(arrX[1]-45),(int)(arrY[1]-10))
cv2.putText(img_color, str(angles[1]) ,place, font , 1, (0,0,255), 1, cv2.LINE_AA)
place = ((int)(arrX[2]-5),(int)(arrY[2]+45))
cv2.putText(img_color, str(angles[2]) ,place, font , 1, (0,0,255), 1, cv2.LINE_AA)

# TODO: plotting the image
plt.imshow(img_color)
plt.axis('off')
plt.show()