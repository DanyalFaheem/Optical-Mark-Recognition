import cv2
import numpy as np
import matplotlib.pyplot as plt


# # TODO : Question 1
# # getting image # 1
# path1 = r'C:\Users\USER\Desktop\Digital Image Processing\Assignment#2\img\Q-1a.jpg'
# img1 = cv2.imread(path1, cv2.IMREAD_GRAYSCALE)
# # getting image # 2
# path2 = r'C:\Users\USER\Desktop\Digital Image Processing\Assignment#2\img\Q-1b.jpg'
# img2 = cv2.imread(path2, cv2.IMREAD_GRAYSCALE)

# # getting the common points of both images by using &(And) operator
# img = img1 & img2

# # getting area
# area = 0
# check1 = True
# # loop to count pixels of the white region
# for i in range(0,img.shape[0]):
#     check2 = True
#     for j in range(0,img.shape[1]):
#         if (img[i][j]==255):
#             area += 1

# # displaying area on image
# font = cv2.FONT_HERSHEY_SIMPLEX
# place = ((int)(50),(int)(50))
# cv2.putText(img, "Area : "+str(area) ,place, font , 1, (255,0,0), 1, cv2.LINE_AA)
# print("Area : ",area)
# # displaying resulting image
# plt.imshow(img,cmap='gray')
# plt.axis('off')
# plt.show()


# for i in range(0,img1.shape[0]):
#     for j in range(0,img1.shape[1]):
#         if (img1[i][j] == img2[i][j] & img1[i][j]==255 & img2[i][j]==255):
#             img1[i][j] = 255
#         else:
#             img1[i][j] = 0

# # TODO question 2 :
# # getting image path
# path = r'C:\Users\USER\Desktop\Digital Image Processing\Assignment#2\img\Q-2.jpg'
# img = cv2.imread(path,cv2.IMREAD_COLOR)

# # using canny to detect the edges
# edge = cv2.Canny(img,100,200)

# # loop to convert the edges into green in original image
# for i in range(0,img.shape[0]):
#     for j in range(0,img.shape[1]):
#         if (edge[i][j]==255):
#             img[i][j] = (0,255,0)

# # plotting the final image
# plt.imshow(img,cmap='gray')
# plt.axis('off')
# plt.show()

# # TODO question 3 :
# # reading the image
# path = r'C:\Users\USER\Desktop\Digital Image Processing\Assignment#2\img\Q-3.jpg'
# img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
# # using sobel operator of x and y direction with kernel size 1
# img2 = cv2.Sobel(img,cv2.CV_64F,2,2,ksize=1)
# plt.imshow(img2,cmap='gray')
# plt.axis('off')
# plt.show()
# # setting the threshold
# ret, thresh1 = cv2.threshold(img2, 100, 255, cv2.THRESH_BINARY)
# plt.imshow(thresh1,cmap='gray')
# plt.axis('off')
# plt.show()
# arrx = [0,0,0]
# arry = [0,0,0]
# count = 0
# index = 0
# # loop to get the corner points
# for i in range(thresh1.shape[0]):
#     for j in range(thresh1.shape[1]):
#         if (thresh1[i][j] == 255):
#             if(count == 0 or count == 1 or count == 6):
#                 arrx[index] = i
#                 arry[index] = j
#                 index += 1
#             count += 1
            

# # calculating area using the corner points
# width = arry[1] - arry[0]
# length = arrx[2] - arrx[0]
# area = length * width

# # displaying area on image
# font = cv2.FONT_HERSHEY_SIMPLEX
# place = ((int)(50),(int)(50))
# cv2.putText(thresh1, "Area : "+str(area) ,place, font , 1, (255,0,0), 1, cv2.LINE_AA)


# # final image of corner points
# plt.imshow(thresh1,cmap='gray')
# plt.axis('off')
# plt.show()
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