# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('barcode_01.jpg')
img2 = cv2.imread('barcode_02.jpg')
img3 = cv2.imread('barcode_03.jpg')
img4 = cv2.imread('barcode_04.jpg')
img5 = cv2.imread('barcode_05.jpg')

#With the code above, we are importing the OpenCV library, and we are reading five pictures that contain barcode.



gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
gray4 = cv2.cvtColor(img4,cv2.COLOR_BGR2GRAY)
gray5 = cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)
plt.subplot(231)
plt.title("Image 1")
plt.imshow(gray1,cmap='gray')
plt.subplot(232)
plt.title("Image 2")
plt.imshow(gray2,cmap='gray')
plt.subplot(233)
plt.title("Image 3")
plt.imshow(gray3,cmap='gray')
plt.subplot(234)
plt.title("Image 4")
plt.imshow(gray4,cmap='gray')
plt.subplot(235)
plt.title("Image 5")
plt.imshow(gray5,cmap='gray')

plt.show()

gradX1 = cv2.Sobel(gray1,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=-1)
#cv2.imshow("gradX1",gradX1)
gradX2 = cv2.Sobel(gray2,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=-1)
#cv2.imshow("gradX2",gradX2)
gradX3 = cv2.Sobel(gray3,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=-1)
#cv2.imshow("gradX3",gradX3)
gradX4 = cv2.Sobel(gray4,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=-1)
#cv2.imshow("gradX4",gradX4)
gradX5 = cv2.Sobel(gray5,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=-1)
#cv2.imshow("gradX5",gradX5)
plt.subplot(231)
plt.title("Image 1")
plt.imshow(gradX1,cmap='gray')
plt.subplot(232)
plt.title("Image 2")
plt.imshow(gradX2,cmap='gray')
plt.subplot(233)
plt.title("Image 3")
plt.imshow(gradX3,cmap='gray')
plt.subplot(234)
plt.title("Image 4")
plt.imshow(gradX4,cmap='gray')
plt.subplot(235)
plt.title("Image 5")
plt.imshow(gradX5,cmap='gray')

plt.show()

gradY1 = cv2.Sobel(gray1,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=-1)
#cv2.imshow("gradY",gradY1)
gradY2 = cv2.Sobel(gray2,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=-1)
#cv2.imshow("gradY",gradY2)
gradY3 = cv2.Sobel(gray3,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=-1)
#cv2.imshow("gradY",gradY3)
gradY4 = cv2.Sobel(gray4,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=-1)
#cv2.imshow("gradY",gradY4)
gradY5 = cv2.Sobel(gray5,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=-1)
#cv2.imshow("gradY",gradY5)
plt.subplot(231)
plt.title("Image 1")
plt.imshow(gradY1,cmap='gray')
plt.subplot(232)
plt.title("Image 2")
plt.imshow(gradY2,cmap='gray')
plt.subplot(233)
plt.title("Image 3")
plt.imshow(gradY3,cmap='gray')
plt.subplot(234)
plt.title("Image 4")
plt.imshow(gradY4,cmap='gray')
plt.subplot(235)
plt.title("Image 5")
plt.imshow(gradY5,cmap='gray')

plt.show()


gradient = cv2.subtract(gradX1,gradY1)
gradient = cv2.convertScaleAbs(gradient)
#cv2.imshow("gradient",gradient)
plt.title("Gradient")
plt.imshow(gradient,cmap='gray')
plt.show()
blurred = cv2.blur(gradient,(9,9))
#cv2.imshow("blured",blurred)
plt.title("Blurred")
plt.imshow(blurred,cmap='gray')
plt.show()

ret, thresh = cv2.threshold(blurred,225,255,cv2.THRESH_BINARY)
#cv2.imshow("thresh",thresh)
plt.title("Thresh")
plt.imshow(thresh,cmap='gray')
plt.show()

se = cv2.getStructuringElement(cv2.MORPH_RECT,(100,7))
closed = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,se)
closed = cv2.erode(closed,None,iterations=4)
closed = cv2.dilate(closed,None,iterations=4)
#cv2.imshow("ds",closed)
plt.title("Closed")
plt.imshow(closed,cmap='gray')
plt.show()

cnts, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
i = sorted(cnts,key=cv2.contourArea,reverse=True)[0]
cv2.drawContours(img1,[i],-1,(0,255,0),3)
#cv2.imshow("img1",img1)
plt.title("Image 1")
plt.imshow(img1,cmap='gray')
plt.show()