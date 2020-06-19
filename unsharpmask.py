import numpy as np
import cv2

img = cv2.imread("dip-xe.tif")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img,(3,3),0)

imggm = img_blur - img

imggm1 = img + 1 * imggm #非锐化掩蔽
imggm2 = img + 2 * imggm #高提升滤波
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        d = img[i][j] + 2 * imggm[i][j]
        if d > 255 : d = 255
        if d < 0 : d = 0
        imggm2[i][j] = d

cv2.imshow('src',img)
cv2.imshow('imggm',imggm)
cv2.imshow('imgblur',img_blur)
cv2.imshow('imggm2',imggm2)

cv2.waitKey()
cv2.destroyAllWindows()
