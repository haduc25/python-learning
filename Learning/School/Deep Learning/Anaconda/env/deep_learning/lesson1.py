# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:15:39 2023

@author: Admin
"""


import cv2
import numpy as np
import os
print(os.getcwd())

 
image = cv2.imread('../img/img2.jpg')  

 


# Print error message if image is null
if image is None:
    print('Could not read image')
 
# Apply identity kernel
kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])
 
identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
 
cv2.imshow('Original', image)
cv2.imshow('Identity', identity)
     
cv2.waitKey()
cv2.imwrite('identity.jpg', identity)
cv2.destroyAllWindows()
 
# case 1 - Apply blurring kernel
kernel2 = np.ones((5, 5), np.float32) / 25
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)
 
cv2.imshow('Original', image)
cv2.imshow('Kernel Blur', img)
     
cv2.waitKey()
cv2.imwrite('blur_kernel.jpg', img)
cv2.destroyAllWindows()

"""
case 2 - Apply blur using `blur()` function 
"""
# img_blur = cv2.blur(src=image, ksize=(5,5)) # Using the blur function to blur an image where ksize is the kernel size
 
# # Display using cv2.imshow()
# cv2.imshow('Original', image)
# cv2.imshow('Blurred', img_blur)
 
# cv2.waitKey()
# cv2.imwrite('blur.jpg', img_blur)
# cv2.destroyAllWindows()


# 
