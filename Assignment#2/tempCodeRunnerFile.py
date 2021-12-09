# TODO question 3 :
# reading the image
path = r'C:\Users\USER\Desktop\Digital Image Processing\Assignment#2\img\Q-3.jpg'
img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
# using sobel operator of x and y direction with kernel size 1
img2 = cv2.Sobel(img,cv2.CV_64F,2,2,ksize=1)
plt.imshow(img2,cmap='gray')
plt.axis('off')
plt.show()
# setting the threshold
ret, thresh1 = cv2.threshold(img2, 100, 255, cv2.THRESH_BINARY)
plt.imshow(thresh1,cmap='gray')
plt.axis('off')
plt.show()
arrx = [0,0,0]
arry = [0,0,0]
count = 0
index = 0
# loop to get the corner points
for i in range(thresh1.shape[0]):
    for j in range(thresh1.shape[1]):
        if (thresh1[i][j] == 255):
            if(count == 0 or count == 1 or count == 6):
                arrx[index] = i
                arry[index] = j
                index += 1
            count += 1
            

# calculating area using the corner points
width = arry[1] - arry[0]
length = arrx[2] - arrx[0]
area = length * width

# displaying area on image
font = cv2.FONT_HERSHEY_SIMPLEX
place = ((int)(50),(int)(50))
cv2.putText(thresh1, "Area : "+str(area) ,place, font , 1, (255,0,0), 1, cv2.LINE_AA)


# final image of corner points
plt.imshow(thresh1,cmap='gray')
plt.axis('off')
plt.show()