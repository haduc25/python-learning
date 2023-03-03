# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:57:29 2023

@author: Admin

[Nguồn tham khảo]
- https://www.geeksforgeeks.org/cnn-introduction-to-pooling-layer/

"""

#  4. Xây dựng chương trình thực hiện gộp (Pooling) trong ảnh.

# =============================================================================
# Max Pooling
# =============================================================================

# import numpy as np
# from keras.models import Sequential
# from keras.layers import MaxPooling2D

# # define input image
# image = np.array([[2, 2, 7, 3],
# 				[9, 4, 6, 1],
# 				[8, 5, 2, 4],
# 				[3, 1, 2, 6]])
# image = image.reshape(1, 4, 4, 1)

# # define model containing just a single max pooling layer
# model = Sequential(
#  	[MaxPooling2D(pool_size = 2, strides = 2)])

# # generate pooled output
# output = model.predict(image)

# # print output image
# output = np.squeeze(output)
# print(output)


# =============================================================================
# Average Pooling
# =============================================================================
# import numpy as np
# from keras.models import Sequential
# from keras.layers import AveragePooling2D

# # define input image
# image = np.array([[2, 2, 7, 3],
# 				[9, 4, 6, 1],
# 				[8, 5, 2, 4],
# 				[3, 1, 2, 6]], dtype=np.float32)
# image = image.reshape(1, 4, 4, 1)

# # define model containing just a single average pooling layer
# model = Sequential(
# 	[AveragePooling2D(pool_size = 2, strides = 2)])

# # generate pooled output
# output = model.predict(image)

# # print output image
# output = np.squeeze(output)
# print(output)


# =============================================================================
# Global Pooling | Lấy kết quả từ Max Pooling& Average Pooling rồi lại tính tiếp
# Max Pooling => 9
# [[9. 7.]
# [8. 6.]]
#
# Average Pooling => 4.0625
# [[4.25 4.25]
# [4.25 3.5 ]]
# =============================================================================
import numpy as np
from keras.models import Sequential
from keras.layers import GlobalMaxPooling2D
from keras.layers import GlobalAveragePooling2D

# define input image
image = np.array([[2, 2, 7, 3],
				[9, 4, 6, 1],
				[8, 5, 2, 4],
				[3, 1, 2, 6]])
image = image.reshape(1, 4, 4, 1)

# define gm_model containing just a single global-max pooling layer
gm_model = Sequential(
	[GlobalMaxPooling2D()])

# define ga_model containing just a single global-average pooling layer
ga_model = Sequential(
	[GlobalAveragePooling2D()])

# generate pooled output
gm_output = gm_model.predict(image)
ga_output = ga_model.predict(image)

# print output image
gm_output = np.squeeze(gm_output)
ga_output = np.squeeze(ga_output)
print("gm_output: ", gm_output) # Max Pooling
print("ga_output: ", ga_output) # Average Pooling












