# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:41:55 2023

@author: Admin
"""

# import cv2
# import numpy as np
# from keras.models import Sequential
# from keras.layers import Conv2D

# # load image in BGR format
# img = cv2.imread('../img/img1.jpg')

# # convert image to RGB format
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# # resize image to (960, 718) shape
# img = cv2.resize(img, (960, 718))

# # convert image to float datatype
# img = img.astype('float32')

# # normalize image to range [0, 1]
# img /= 255

# # add batch dimension
# img = np.expand_dims(img, axis=0)

# # create Conv2D model
# model = Sequential()
# model.add(Conv2D(filters=3, kernel_size=(3, 3), strides=(2, 2), padding='valid', input_shape=img.shape[1:]))

# # predict output
# output = model.predict(img)

# # show original and pooled images
# cv2.imshow('Original', img[0])
# cv2.imshow('Pooled', output[0])
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D

# load image in BGR format
# img = cv2.imread('../img/img2.jpg')
img = cv2.imread('../img/img2.jpg', cv2.IMREAD_COLOR)

# convert image to RGB format
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
img = cv2.cvtColor(img, cv2.COLOR_YUV2RGB)


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

# show original and pooled images
cv2.imshow('Original', img[0])
cv2.imshow('Pooled', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

