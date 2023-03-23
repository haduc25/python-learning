# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:40:38 2023

@author: Admin
"""

import cv2
import face_recognition
import os
import tqdm

# =============================================================================
# STEP 1: LOAD IMAGE FROM FOLDER (IMAGE FOR TRAINING) 
# =============================================================================

# path
pathFolder = 'img/library'

# create empty array
images = []
classNames = []

# create a list => load image from folder to list
myList = os.listdir(pathFolder)
print('myList: ', myList) # ['Ban_Mai_Huyen_1.jpg', 'Do_Mai_Lan_1.jpg', 'Do_Mai_Lan_2.jpg', 'Nguyen_Tu_Anh_1.jpg', 'Nguyen_Tu_Anh_2.jpg']


# loop get image 1 by 1
for imgName in myList:
    print('image: ', imgName)
    """
    image:  Ban_Mai_Huyen_1.jpg
    image:  Do_Mai_Lan_1.jpg
    image:  Do_Mai_Lan_2.jpg
    image:  Nguyen_Tu_Anh_1.jpg
    image:  Nguyen_Tu_Anh_2.jpg
    """
    
    # current iamge - ảnh hiện tại | đọc từng ảnh 1 => đẩy ma trận điểm ảnh (image) vào array 'images'
    curImage = cv2.imread(f'{pathFolder}/{imgName}') #img/library/imgName == 'Ban_Mai_Huyen_1.jpg', 'Do_Mai_Lan_1.jpg', 'Do_Mai_Lan_2.jpg', 'Nguyen_Tu_Anh_1.jpg', 'Nguyen_Tu_Anh_2.jpg'
    
    # add 'curImage' to array 'images' | arr.append()
    images.append(curImage)

    """ os.path.splitext(imgName)[0] | splittext(): tách path ra thành 2 phần: 1. trước phần đuôi mở rộng (fileName), 2. phần đuôi mở rộng (ext) 
        # tách tên file vs đuôi file ra (test.txt => ['test', '.txt]) => exam-splitText.py
        # tách ra & append() to array 'classNames'
        # os.path.splitext(imgName)[0]: cắt ra lấy phần tên | Ban_Mai_Huyen_1.jpg => lấy phần 'Ban_Mai_Huyen_1' & bỏ '.jpg' => '.jpg' ở index 1 
        # => lấy image name => bỏ ext (đuôi file) => add cái image name và trong array 'classNames' => arr.append()
    """
    classNames.append(os.path.splitext(imgName)[0])
    

# print length of array
print('\nlength of array images is', len(images)) # 5   
print('className is', classNames) # ['Ban_Mai_Huyen_1', 'Do_Mai_Lan_1', 'Do_Mai_Lan_2', 'Nguyen_Tu_Anh_1', 'Nguyen_Tu_Anh_2']
    
    
# =============================================================================
# STEP 2: ENCODE IMAGE
# =============================================================================

def encodeImage(images):
    # create a empty array 
    encodeList = []    
    
    # loop to get element in images
    for img in images:
        # convert from BGR to RGB => cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # encode image => face_recognition.face_encodings()
        # face_recognition.face_encodings(img)[0] => index = 0 vì vẫn chạy từng image 1
        encodeImg = face_recognition.face_encodings(img)[0]
    
        # add image encodeed to array 'encodeList'
        encodeList.append(encodeImg)
        
        
    # print
    print('\n\n################## ENCODED SUCCESS ##################\n\n')
    
    return encodeList


# encodeImage custom have progressbar from chatGPT + F8
def encodeImageCustom(images):
    # create an empty array
    encodeList = []

    # get the length of the images list
    num_images = len(images)

    # loop to get element in images
    for i, img in enumerate(images):
        # convert from BGR to RGB => cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # encode image => face_recognition.face_encodings()
        # face_recognition.face_encodings(img)[0] => index = 0 vì vẫn chạy từng image 1
        encodeImg = face_recognition.face_encodings(img)[0]

        # add image encoded to array 'encodeList'
        encodeList.append(encodeImg)

        # calculate the progress as a percentage
        progress = (i + 1) / num_images * 100

        # print the progress
        print(f"Progressing: {int(progress)}%")

    # print
    print('\n\n################## ENCODED SUCCESS ##################\n\n')

    return encodeList


# custom using lib tqdm
def encodeImageCustom2(images):
    # create an empty array
    encodeList = []

    # create a tqdm progress bar
    progress_bar = tqdm.tqdm(total=len(images), desc="Encoding images...", unit="image")

    # loop to get element in images
    for img in images:
        # convert from BGR to RGB => cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # encode image => face_recognition.face_encodings()
        # face_recognition.face_encodings(img)[0] => index = 0 vì vẫn chạy từng image 1
        encodeImg = face_recognition.face_encodings(img)[0]

        # add image encoded to array 'encodeList'
        encodeList.append(encodeImg)

        # update the progress bar
        progress_bar.update()

    # close the progress bar
    progress_bar.close()

    # print
    print('\n\n################## ENCODED SUCCESS ##################\n\n')

    return encodeList


# Encrypted image list | Danh sách hình ảnh đã được mã hóa
# encryptedImageList = encodeImage(images)
# encryptedImageList = encodeImageCustom(images)
encryptedImageList = encodeImageCustom2(images)

# length of encryptedImageList
print('length of encryptedImageList is', len(encryptedImageList))


# =============================================================================
# Using webcam
# =============================================================================

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()  # đọc img & return về ret => True/False, frame => khung hình
    
    # checking webcam is being used or not?
    if not ret:
        print('\n\n\nWebcam đang được sử dụng!\n\n\n')
        break
    
    # resize frame
    """
        cv2.resize(frame, (0, 0), None, fx=.5, fy=.5)\
        (0, 0) => dsize
        None => dst
        fx=.5, fy=.5 => kích thước = 50% image ban đầu
    """
    frameResized = cv2.resize(frame, (0, 0), None, fx=.5, fy=.5)
    
    
    # Convert BGR => RGB
    frameResized = cv2.cvtColor(frameResized, cv2.COLOR_BGR2RGB)
    
    """ face current frame | current face position on frame (vị trí khuôn mặt hiện tại trên khung hình)
        - xác định vị trí khuôn mặt hiện tại trên webcam => face_recognition.face_locations()
    """

    currentFacePositionOnFrame = face_recognition.face_locations(frameResized) # lấy khuôn mặt & vị trí khuôn mặt hiện tại
    
    # Encode current face on Webcam => face_recognition.face_encodings()
    encodeCurrentFaceOnWebcam = face_recognition.face_encodings(frameResized)
    
    # show img
    cv2.imshow('My Capture', frameResized)

    # waiting key / 1s
    if (cv2.waitKey(1) == ord('q')):
        break
    

# exit camera
capture.release()

# close window
cv2.destroyAllWindows()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    