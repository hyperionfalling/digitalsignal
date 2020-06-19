#!/usr/bin/env python  
#-*- coding: utf-8 -*-  

__author__ = 'wts'  
  
import cv2  
import os  
from scipy import interpolate
import scipy.misc
from PIL import Image
import imageio
import numpy as np
  
if __name__ == '__main__':  
    img = cv2.imread("dcolor.jpeg") 
    #cv2.imshow("Original", img)      
    height, width = img.shape[:2]  

    # 放大图像  
    fx = np.sqrt(2)  
    fy = np.sqrt(2)  
    
    enlarge_nearest = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_NEAREST)
    enlarge_linear = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR) 
    enlarge_cubic = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC) #双三次/三次卷积
    enlarge_spline = scipy.misc.imresize(img, np.sqrt(2.0), interp='cubic')
    
  
    # 显示  
    cv2.imshow("origin", img)  
    cv2.imshow("nearest", enlarge_nearest)  
    cv2.imshow("linear", enlarge_linear) 
    cv2.imshow("cubic", enlarge_cubic) 
    cv2.imshow("spline", enlarge_spline) 
    
  
    cv2.waitKey(0)  
    

