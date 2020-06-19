import cv2
import numpy as np
from scipy import signal

img = cv2.imread('moon.tif')

img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

myh1=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
myh2=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
myh3=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])

dstr1 = cv2.filter2D(img,-1,myh1)
dstr2 = cv2.filter2D(img,-1,myh2)
dstr3 = cv2.filter2D(img,-1,myh3)

lapla1 = img + dstr1
lapla2 = img + dstr2
lapla3 = img + dstr3

cv2.imshow('src',img)
cv2.imshow('laplacian1',lapla1)
cv2.imshow('laplacian2',lapla2)
cv2.imshow('laplacian3',lapla3)
cv2.waitKey()
cv2.destroyAllWindows()

