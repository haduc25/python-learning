# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:40:04 2023

@author: Admin
"""

# 2. Xây dựng chương trình thực hiện đệm (Padding) trong ảnh.
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



# using copyMakeBorder(src, top, bottom, left, right, borderType = cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT, value = rgb())
imageHasBorder = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value = (0, 255, 255))


cv2.imshow('Original', image)
cv2.imshow('image has border', imageHasBorder)

cv2.waitKey()
cv2.imwrite('../imgExported/imageHasBorder.jpg', imageHasBorder)
cv2.destroyAllWindows()

# using copyMakeBorder - BORDER_CONSTANT
imageHasBorderRef = cv2.copyMakeBorder(image, 100, 100, 50, 50, cv2.BORDER_REFLECT)


cv2.imshow('Original', image)
cv2.imshow('image has border reflect', imageHasBorderRef)

cv2.waitKey()
cv2.imwrite('../imgExported/imageHasBorder.jpg', imageHasBorderRef)
cv2.destroyAllWindows()














