import cv2
import numpy as np
import matplotlib.pyplot as plt
path = r"C:\Users\USER\Desktop\Digital Image Processing\Optical-Mark-Recognition\Dataset\unnamed (4).jpg"
img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
# TODO : Reading the image again in coloured mode
img_color = cv2.imread(path,cv2.IMREAD_COLOR)
# img = img - 255
img_color = img_color[3770:7200, 2141:4500]
img = img[3770:7210, 2141:4500]
img = cv2.GaussianBlur(img,(3,3),1,0)
thresh, out = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
# edged = cv2.Canny(out, 30, 200)
out = out - 255
contours, hierarchy = cv2.findContours(out,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print (len(contours))
# print(contours)
# TODO : Drawing contours
temp = np.zeros_like(img_color)
cv2.drawContours(temp,contours,-1,(0,255,0),3)

# cv2.imshow('Contours', out)
# cv2.waitKey(0)
# cv2.destroyAllWindows

plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()
plt.imshow(out, cmap='gray')
plt.axis('off')
plt.show()
plt.imshow(temp, cmap='gray')
plt.axis('off')
plt.show()