import cv2
import numpy as np
import matplotlib.pyplot as plt

# TODO question 4 :
# reading the image
path = r'C:\Users\USER\Desktop\Digital Image Processing\Assignment#2\img\Q-4.jpg'
img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
# getting the negative of the image
img2 = 255 - img
plt.imshow(img2,cmap='gray')
plt.axis('off')
plt.show()
# setting the kernel of the image
kernel = np.ones((1, 20), np.uint8)
# Eroding the image 4 times
img2 = cv2.erode(img2,kernel,iterations=1)
plt.imshow(img2,cmap='gray')
plt.axis('off')
plt.show()
img2 = cv2.erode(img2,kernel,iterations=1)
plt.imshow(img2,cmap='gray')
plt.axis('off')
plt.show()
img2 = cv2.erode(img2,kernel,iterations=1)
plt.imshow(img2,cmap='gray')
plt.axis('off')
plt.show()
img2 = cv2.erode(img2,kernel,iterations=1)
plt.imshow(img2,cmap='gray')
plt.axis('off')
plt.show()
# DIlating the image 1 time
img2 = cv2.dilate(img2,kernel,iterations=1)
plt.imshow(img2,cmap='gray')
plt.axis('off')
plt.show()
# Getting the negative of the final image
img2 = 255 - img2
# ploting the final image
plt.imshow(img2,cmap='gray')
plt.axis('off')
plt.show()