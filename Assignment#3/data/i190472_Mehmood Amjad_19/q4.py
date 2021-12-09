# References
# 1- Code provided by Dr. Akhtar Jamil (code 6 case study)
# 2- Code provided by Dr. Akhtar Jamil (code 11)
# 3- https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html
import cv2
import numpy as np
import matplotlib.pyplot as plt

# TODO: Reading Video
path = r'C:\Users\USER\Desktop\Digital Image Processing\Assignment#3\data\animation.mp4'

cap = cv2.VideoCapture(path)
fps = cap.get(cv2.CAP_PROP_FPS)
fps = int(fps)
arrY = []
check = True
# TODO: Loop till end of video
while(cap.isOpened()):
    # TODO: Read frame by frame
    ret, frame = cap.read()
    if ret == True:
        # TODO: reading frame in grayscale mode
        img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # TODO: getting negative of the image
        img = 255 - img
        # TODO: Applying threshold on the image (the threshold value was generated on hit and run basis)
        threshold, bw = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)  

        # TODO: Finding Contours
        contours, hierarchy = cv2.findContours(bw,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        # TODO: Getting the centers of the circles (code provided by dr Akhtar Jamil)
        for i in range(len(contours)):
            M = cv2.moments(contours[i])
            x = int(M["m10"] / M["m00"])
            y = int(M["m01"] / M["m00"])
            # TODO: appending the latest y-axis of the centers of the contours only as x-axis remains the same
            arrY.append(y)
        
        cv2.imshow('Video', frame)
        # TODO: Comparing the center circle with the latest axis of outer circle
        if arrY[0] == arrY[len(arrY)-1]:
            # stops the screen until any key is pressed
            cv2.waitKey(0)        
        if cv2.waitKey(fps) & 0xFF == ord('q'):
                break
    else:
        break
        cv2.destroyAllWindows()

cv2.destroyAllWindows()
cap.release()
print('Video Object Released.')