# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 12:04:36 2021

@author: user

"""
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# import image
im = cv.imread('image/silliconvelly.jpg')


# BGR
plt.figure()
plt.imshow(im)
plt.title('Original')

# RGB
rgb = cv.cvtColor(im, cv.COLOR_BGR2RGB) # cvt = convert
plt.figure()
plt.imshow(rgb)
plt.title('RGB')


# gray scale
gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(gray,cmap='gray') # essential cmap
plt.title('GRAY')


# blur
blur = cv.blur(im,(10,10)) # 블러시 청크 사이즈 숫자가 작으수록 선명
blur = cv.cvtColor(blur, cv.COLOR_BGR2RGB)
plt.subplot(121) # 1행2열 로 나눔 그리고 첫번째를 가리킴
plt.imshow(rgb)
plt.title('RGB')
plt.subplot(122) # 1행 2열중 두번째를 가리킴
plt.imshow(blur)
plt.title('Blur')


# dege detection # 머신러닝에서 유용하게 활용
edges =  cv.Canny(gray,200,300)
plt.subplot(121) 
plt.imshow(gray, cmap='gray')
plt.title('Gray')
plt.subplot(122) 
plt.imshow(edges, cmap='gray')
plt.title('Edge Detection')