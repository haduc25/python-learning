# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 23:16:53 2023

@author: Admin
"""
# from keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np
# import os

# # Load the pre-trained model
# model_path = "./Cat_vs_Dog-CNN.model"

# if os.path.exists(model_path):
#     # Model exists in the current directory
#     # Load the model
#     print('Model found in directory.')
#     model = load_model(model_path)
# else:
#     # Model does not exist in the current directory
#     print('Model not found in directory. Please train the model first.')
#     exit()

# # Load an image to classify
# img_path = 'unknown/con_gi_day3.jpg'

# if os.path.exists(img_path):
#     # Image exists in the current directory
#     img = image.load_img(img_path, target_size=(50, 50))
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)

#     # Make a prediction
#     preds = model.predict(x)
#     if preds[0][0] == 1:
#         print("It's a dog!")
#     else:
#         print("It's a cat!")
# else:
#     print('Image not found in directory.')

from keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Load the pre-trained model
model_path = "./Cat_vs_Dog-CNN.model"

if os.path.exists(model_path):
    # Model exists in the current directory
    # Load the model
    print('have folder trained!')
    model = load_model(model_path)
    print('loaded model!')
else:
    # Model does not exist in the current directory
    # Train the model
    model = train_model()
    print('Need to train!')

# Load an image to classify
img_path = 'unknown/con_gi_day4.jpg'

if os.path.exists(img_path):
    print('have file image!')
else:
    print('dont have file')

# Resize the image and convert it to grayscale
img = image.load_img(img_path, target_size=(50, 50), color_mode='grayscale')
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

# Normalize the pixel values
x = x.astype('float32') / 255

# Make a prediction
preds = model.predict(x)
if preds[0][0] == 1:
    print("It's a dog!")
else:
    print("It's a cat!")



    
