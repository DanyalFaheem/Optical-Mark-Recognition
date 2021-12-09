import cv2
import numpy as np
import matplotlib.pyplot as plt


# TODO : Question 1
# getting image # 1
path1 = r'C:\Users\USER\Desktop\Digital Image Processing\Assignment#2\img\Q-1a.jpg'
img1 = cv2.imread(path1, cv2.IMREAD_GRAYSCALE)
# getting image # 2
path2 = r'C:\Users\USER\Desktop\Digital Image Processing\Assignment#2\img\Q-1b.jpg'
img2 = cv2.imread(path2, cv2.IMREAD_GRAYSCALE)

# getting the common points of both images by using &(And) operator
img = img1 & img2

# getting area
area = 0
check1 = True
# loop to count pixels of the white region
for i in range(0,img.shape[0]):
    check2 = True
    for j in range(0,img.shape[1]):
        if (img[i][j]==255):
            area += 1

# displaying area on image
font = cv2.FONT_HERSHEY_SIMPLEX
place = ((int)(50),(int)(50))
cv2.putText(img, "Area : "+str(area) ,place, font , 1, (255,0,0), 1, cv2.LINE_AA)
print("Area : ",area)
# displaying resulting image
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.show()