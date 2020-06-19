import cv2
import numpy as np
from matplotlib import pyplot as plt

#读取图像
img = cv2.imread('a.tif', 0)

#傅里叶变换
dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
fshift = np.fft.fftshift(dft)

#设置低通滤波器
rows, cols = img.shape
crow,ccol = int(rows/2), int(cols/2) #中心位置
res = [img, img, img, img, img]

m = [5, 10, 30, 90, 270]
for i in range(0,5):

    mask = np.zeros((rows, cols, 2), np.uint8)
    mask[crow-m[i]:crow+m[i], ccol-m[i]:ccol+m[i]] = 1

    #掩膜图像和频谱图像乘积
    f = fshift * mask
    #print(f.shape, fshift.shape, mask.shape)

    #傅里叶逆变换
    ishift = np.fft.ifftshift(f)
    iimg = cv2.idft(ishift)
    res[i] = cv2.magnitude(iimg[:,:,0], iimg[:,:,1])

#显示原始图像和低通滤波处理图像
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
