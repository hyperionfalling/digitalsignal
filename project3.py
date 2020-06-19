import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import e

img = cv2.imread('Fig0308.tif')
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgtest = 255 - img
imgtest1 = 0.1 * img

def log(c, img):
    output = c * np.log(1.0 + img)
    output = np.uint8(output + 0.5)
    return output

def log_plot(c):
    x = np.arange(0, 256, 0.01)
    y = c * np.log(x + 1)
    plt.plot(x, y, 'r', linewidth=1)
    plt.rcParams['font.sans-serif']=['SimHei'] 
    plt.title('log')
    plt.xlim(0, 255), plt.ylim(0, 255)
    plt.show()

    
def gamma(img, c, v):
    lut = np.zeros(256, dtype = np.float32)
    for i in range(256):
        lut[i] = c * i ** v
    out_img = cv2.LUT(img, lut)
    ou_img = np.uint8(out_img + 0.5)
    return out_img

def gamma_plot(c, v):
    x = np.arange(0, 256, 0.01)
    y = c * x ** v
    plt.plot(x, y, 'r', linewidth=1)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.title('gamma')
    plt.xlim([0, 255]), plt.ylim([0, 1.5])
    plt.show()

#ta40 = log(40, imggray) 
#tb0108_0_5 = gamma(imggray, 0.08, 0.5)
#log_plot(40)
gamma_plot(0.08, 0.5)

'''
ta16 = log(16, imggray)
ta40 = log(40, imggray) #best
ta64 = log(64, imggray)

cv2.imshow("gray", imggray)
cv2.imshow("c 16", ta16)
cv2.imshow("c 40", ta40)
cv2.imshow("c 64", ta64)


tb0108_0_5 = gamma(imggray, 0.08, 0.5) #best
tb0108_1 = gamma(imggray, 0.08, 1)
tb0108_0_1 = gamma(imggray, 0.08, 0.1)
tb08_0_5 = gamma(imggray, 0.8, 0.5)
tb0308_0_5 = gamma(imggray, 0.0008, 0.5)

cv2.imshow("tb0108_0_5", tb0108_0_5)
cv2.imshow("tb0108_1", tb0108_1)
cv2.imshow("tb0108_0_1", tb0108_0_1)
cv2.imshow("tb08_0_5", tb08_0_5)
cv2.imshow("tb0308_0_5", tb0308_0_5)

plt.figure("origin")
arr = imggray.flatten()
plt.hist(arr, bins=256, normed=1, facecolor='red', label="ori")  


plt.figure("log trans")
arr1 = ta40.flatten()
plt.hist(arr1, bins=256, normed=1, facecolor='green', label="log")  

plt.figure("power-low trans")
arr2 = tb0108_0_5.flatten()
plt.hist(arr2, bins=256, normed=1, facecolor='blue', label="gamma")  
'''
#plt.show()

#cv2.waitKey(0)












