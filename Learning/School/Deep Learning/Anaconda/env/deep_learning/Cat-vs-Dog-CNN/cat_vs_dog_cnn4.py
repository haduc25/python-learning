# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 21:40:01 2023

@author: Admin
"""
# import cv2
# import tensorflow as tf
# import os

# CATEGORIES = ["Cat", "Dog"]

# def prepare(filepath):
#     IMG_SIZE = 50
#     img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
#     new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    
#     ######################
#     cv2.imshow('Precdiction Image', img_array)
#     cv2.waitKey()
   
#     cv2.destroyAllWindows()
#     ######################
#     return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

# model_path = 'Cat_vs_Dog-CNN.model'

# if os.path.exists(model_path):
#     # Model exists in the current directory
#     # Load the model
#     print('have folder trained!')
#     model = tf.keras.models.load_model(model_path)
#     print('loaded model!')
    
        
#     prediction = model.predict([prepare('unknown/con_gi_day4.jpg')])
    
#     print(CATEGORIES[int(prediction[0][0])])
# else:
#     # Model does not exist in the current directory
#     # Train the model
#     # model = train_model()
#     print('Need to train!')

##########################################
# import cv2
# import tensorflow as tf
# import os


# CATEGORIES = ["Cat", "Dog"]

# def prepare(filepath):
#     IMG_SIZE = 50
#     img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
#     new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    
#     ######################
#     cv2.imshow('Precdiction Image', img_array)
#     cv2.waitKey()
   
#     cv2.destroyAllWindows()
#     ######################
#     return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

# model_path = 'Cat_vs_Dog-CNN.model'

# if os.path.exists(model_path):
#     # Model exists in the current directory
#     # Load the model
#     print('have folder trained!')
#     model = tf.keras.models.load_model(model_path)
#     print('loaded model!')
    
#     # Load the test data
#     test_data =  # load your test data
    
#     # Evaluate the model on the test data
#     loss, accuracy = model.evaluate(test_data)
#     print('Test loss:', loss)
#     print('Test accuracy:', accuracy)
        
#     prediction = model.predict([prepare('unknown/con_gi_day4.jpg')])
    
#     print(CATEGORIES[int(prediction[0][0])])
# else:
#     # Model does not exist in the current directory
#     # Train the model
#     # model = train_model()
#     print('Need to train!')


################################################################

# from tensorflow.keras.preprocessing.image import ImageDataGenerator

# train_dir = "PetImages/"
# # test_datagen = ImageDataGenerator(rescale=1./255)
# train_datagen = ImageDataGenerator(
#         rescale=1./255,
#         shear_range=0.2,
#         zoom_range=0.2,
#         horizontal_flip=True)

# IMG_SIZE = 50
    
# train_data = train_datagen.flow_from_directory(
#         train_dir,
#         target_size=(IMG_SIZE, IMG_SIZE),
#         batch_size=32,
#         class_mode='binary')

###########################

import cv2
import tensorflow as tf
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator


CATEGORIES = ["Cat", "Dog"]

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

def prepare(filepath):
    IMG_SIZE = 50
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    
    ######################
    cv2.imshow('Precdiction Image', img_array)
    cv2.waitKey()
   
    cv2.destroyAllWindows()
    ######################
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model_path = 'Cat_vs_Dog-CNN.model'

if os.path.exists(model_path):
    # Model exists in the current directory
    # Load the model
    print('have folder trained!')
    model = tf.keras.models.load_model(model_path)
    print('loaded model!')
    
    # Load the test data
    test_data = train_datagen.flow_from_directory(
            train_dir,
            target_size=(IMG_SIZE, IMG_SIZE),
            batch_size=32,
            class_mode='binary')
    
    # Evaluate the model on the test data
    loss, accuracy = model.evaluate(test_data)
    print('Test loss:', loss)
    print('Test accuracy:', accuracy)
        
    prediction = model.predict([prepare('unknown/con_gi_day4.jpg')])
    
    print(CATEGORIES[int(prediction[0][0])])
else:
    # Model does not exist in the current directory
    # Train the model
    # model = train_model()
    print('Need to train!')

    
