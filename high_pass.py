import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#读取图像
img = cv.imread('a.tif', 0)

#傅里叶变换
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

#设置高通滤波器
rows, cols = img.shape
crow,ccol = int(rows/2), int(cols/2)
res = [img, img, img, img, img]

m = [5, 10, 30, 90, 270]
for i in range(0,5):
    fshift[crow-m[i]:crow+m[i], ccol-m[i]:ccol+m[i]] = 0

    #傅里叶逆变换
    ishift = np.fft.ifftshift(fshift)
    iimg = np.fft.ifft2(ishift)
    iimg = np.abs(iimg)
    res[i] = iimg

#显示原始图像和高通滤波处理图像
plt.subplot(231), plt.imshow(img, 'gray'), plt.title('Original Image')
plt.axis('off')
plt.subplot(232), plt.imshow(res[0], 'gray'), plt.title('Result Image 5')
plt.axis('off')
plt.subplot(233), plt.imshow(res[1], 'gray'), plt.title('Result Image 10')
plt.axis('off')
plt.subplot(234), plt.imshow(res[2], 'gray'), plt.title('Result Image 30')
plt.axis('off')
plt.subplot(235), plt.imshow(res[3], 'gray'), plt.title('Result Image 90')
plt.axis('off')
plt.subplot(236), plt.imshow(res[4], 'gray'), plt.title('Result Image 270')
plt.axis('off')
plt.show()
