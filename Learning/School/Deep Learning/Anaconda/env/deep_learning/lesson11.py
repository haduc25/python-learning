# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:46:01 2023

@author: Admin
"""
#

import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D

# load image in BGR format
# img = cv2.imread('../img/img2.jpg')
img = cv2.imread('../img/img2.jpg', cv2.IMREAD_COLOR)

# convert image to RGB format
def convert_bgr_to_rgb(img):
    if len(img.shape) == 3 and img.shape[2] == 3:
        if img[..., 0].mean() < 1 or img[..., 2].mean() < 1:
            return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

img = convert_bgr_to_rgb(img)

# resize image to (960, 718) shape
img = cv2.resize(img, (960, 718))

# convert image to float datatype and normalize to range [0, 1]
img = img.astype('float32') / 255

# add batch dimension
img = np.expand_dims(img, axis=0)

# create Conv2D model with 3 filters (for RGB)
model = Sequential()
model.add(Conv2D(filters=3, kernel_size=(3, 3), strides=(2, 2), padding='valid', input_shape=img.shape[1:]))

# predict output
output = model.predict(img)

# convert output to uint8 datatype and scale back to range [0, 255]
output = np.uint8(output[0] * 255)

#%%
# show original and pooled images
cv2.imshow('Original', img[0])
cv2.imshow('Pooled', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%%

