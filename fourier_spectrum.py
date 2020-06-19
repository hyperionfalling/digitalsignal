import cv2
import numpy as np
import matplotlib.pyplot as plt
img1=cv2.imread('a.tif',0)
dft=cv2.dft(np.float64(img1),flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=np.fft.fftshift(dft)
magnitude_spectrum=20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
plt.subplot(1,2,1),plt.imshow(img1)
plt.title('input image'),plt.xticks([]),plt.yticks([])
plt.subplot(1,2,2),plt.imshow(magnitude_spectrum)
plt.title('magnitude spectrum'),plt.xticks([]),plt.yticks([])
plt.show()

sum1 = np.sum(np.abs(dft_shift)) / (img1.shape[0] * img1.shape[1])
print(sum1)
