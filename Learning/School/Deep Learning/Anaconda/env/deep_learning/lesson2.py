# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:15:39 2023

@author: Admin
"""


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
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

print('Resized Dimestions: ', resized.shape)

cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
