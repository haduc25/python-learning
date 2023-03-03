# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:29:00 2023

@author: Admin
"""
import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import AveragePooling2D

# load image in grayscale
img = cv2.imread('../img/img2.jpg', cv2.IMREAD_GRAYSCALE)

# resize image to (960, 718) shape
img = cv2.resize(img, (960, 718))

# convert image to float datatype
img = img.astype('float32')

# normalize image to range [0, 1]
img /= 255

# add channel dimension
img = np.expand_dims(img, axis=-1)

# create AveragePooling2D model
model = Sequential()
model.add(AveragePooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid', input_shape=img.shape))

# predict output
output = model.predict(img[np.newaxis, ...])

# show original and pooled images
cv2.imshow('Original', img[..., 0])
cv2.imshow('Pooled', output[0, ..., 0])
cv2.waitKey(0)
cv2.destroyAllWindows()


