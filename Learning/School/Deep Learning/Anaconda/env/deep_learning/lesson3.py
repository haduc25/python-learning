# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:15:13 2023

@author: Admin
"""

#   1. Xây dựng chương trình thực hiện phép tích chập (Convolution) trong ảnh.
import cv2
import numpy as np

image = cv2.imread('../img/img2.jpg')  

 


# Print error message if image is null
if image is None:
    print('Could not read image')
    
# scale
scale_percent = 60
w = int(image.shape[1] * scale_percent / 100)
h = int(image.shape[0] * scale_percent / 100)
dim = (w, h)

# resize image
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
 
# Apply identity kernel
kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])
 
identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
 
cv2.imshow('Original', image)
cv2.imshow('Identity', identity)
     
cv2.waitKey()
cv2.imwrite('../imgExported/identity.jpg', identity)
cv2.destroyAllWindows()
 
# Apply blurring kernel
kernel2 = np.ones((5, 5), np.float32) / 25
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)
 
cv2.imshow('Original', image)
cv2.imshow('Kernel Blur', img)
     
cv2.waitKey()
cv2.imwrite('../imgExported/blur_kernel.jpg', img)
cv2.destroyAllWindows()

# Laplacian 
kernel3 = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype="int")
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel3)
 
cv2.imshow('Original', image)
cv2.imshow('Kernel Laplacian', img)
     
cv2.waitKey()
cv2.imwrite('../imgExported/Laplacian.jpg', img)
cv2.destroyAllWindows()


# Sharpen  
kernel4 = np.array((
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]), dtype="int")
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel4)
 
cv2.imshow('Original', image)
cv2.imshow('Sharpen Laplacian', img)
     
cv2.waitKey()
cv2.imwrite('../imgExported/Sharpen.jpg', img)
cv2.destroyAllWindows()











