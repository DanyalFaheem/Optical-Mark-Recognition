import cv2
import numpy as np
import matplotlib.pyplot as plt

# TODO question 2 :
# getting image path
path = r'C:\Users\USER\Desktop\Digital Image Processing\Assignment#2\img\Q-2.jpg'
img = cv2.imread(path,cv2.IMREAD_COLOR)

# using canny to detect the edges
edge = cv2.Canny(img,100,200)

# loop to convert the edges into green in original image
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if (edge[i][j]==255):
            img[i][j] = (0,255,0)

# plotting the final image
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.show()