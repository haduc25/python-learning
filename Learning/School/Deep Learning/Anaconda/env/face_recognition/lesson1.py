# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:35:54 2023

@author: Admin
"""

import face_recognition
import cv2

# load img
imgMaiLan = face_recognition.load_image_file(
    'img/classify/do_mai_lan/dml1.jpg')

# Chuyển BGR => RGB
# imgMaiLan = cv2.cvtColor(imgMaiLan, cv2.COLOR_BGR2RGB)


# image cần nhận diện
# unknownImg = face_recognition.load_image_file(
#     'img/classify/do_mai_lan/dml2.jpg')

# example other image 
# unknownImg = face_recognition.load_image_file(
    # 'img/classify/nguyen_tu_anh/nta1.jpg')

unknownImg = face_recognition.load_image_file(
    'img/classify/nguyen_tu_anh/nta2.jpg')

# Chuyển BGR => RGB
# imgMaiLan = cv2.cvtColor(imgMaiLan, cv2.COLOR_BGR2RGB)

# =============================================================================
# Xác định vị trí khuôn mặt
# =============================================================================

faceLocation = face_recognition.face_locations(
    imgMaiLan)[0]  # vì đang có 1 image => cho index = 0

# print inmage
# (110, 726, 665, 171) | (y1, x2, y2, x1)
print('faceLocation is ', faceLocation)

# mã hóa image - encode
encodeMailan = face_recognition.face_encodings(imgMaiLan)[0]

# vẽ hình chữ nhật
"""
 # (110, 726, 665, 171) | (y1, x2, y2, x1) | (0, 1, 2, 3) => index
 # pt1
 # faceLocation[3]: điểm bắt đầu (x1)
 # faceLocation[0]: điểm bắt đầu (y1) 
 
 # pt2
 # faceLocation[1]: điểm kết thúc (x1)
 # faceLocation[2]: điểm kết thúc (y1) 
"""
cv2.rectangle(imgMaiLan, (faceLocation[3], faceLocation[0]), (faceLocation[1], faceLocation[2]), (0, 255, 0), 2)

# =============================================================================
# Handle with unknown image
# =============================================================================

# lấy vị trí face, mã hóa, vẽ hình chữ nhật cho unknown image
unknownFaceLocation = face_recognition.face_locations(
    unknownImg)[0]
encodeUnknowImg = face_recognition.face_encodings(unknownImg)[0]
cv2.rectangle(unknownImg, (unknownFaceLocation[3], unknownFaceLocation[0]), (unknownFaceLocation[1], unknownFaceLocation[2]), (255, 0, 0), 2)

# =============================================================================
# CASE 1 - resize image & combine 2 image in 1 window
# =============================================================================

# # Resize the images to have the same height (optional)
# height = min(imgMaiLan.shape[0], unknownImg.shape[0])
# imgMaiLan = cv2.resize(imgMaiLan, (int(imgMaiLan.shape[1]*height/imgMaiLan.shape[0]), height))
# unknownImg = cv2.resize(unknownImg, (int(unknownImg.shape[1]*height/unknownImg.shape[0]), height))


# =============================================================================
# CASE 2 - resize image (size = 50%) & combine 2 image in 1 window
# =============================================================================

# Calculate the desired width for each image
# width = min(int(imgMaiLan.shape[1]*0.5), int(unknownImg.shape[1]*0.5)) # 50%
width = min(int(imgMaiLan.shape[1]*0.8), int(unknownImg.shape[1]*0.8)) # 80%

# Resize the images to the desired width
imgMaiLan = cv2.resize(imgMaiLan, (width, int(imgMaiLan.shape[0]*width/imgMaiLan.shape[1])))
unknownImg = cv2.resize(unknownImg, (width, int(unknownImg.shape[0]*width/unknownImg.shape[1])))


# =============================================================================
# So sánh image/ compare => face_recognition.compare_faces(known_face_encodings, face_encoding_to_check)
# =============================================================================

imgResult = face_recognition.compare_faces([encodeMailan], encodeUnknowImg)

print('imgResult: ', imgResult) # True / False

# =============================================================================
# So sánh khi có nhiều ảnh: khoảng cách (sai số) giữa các bức ảnh? 
# => face_recognition.face_distance(face_encodings, face_to_compare) | distance
# faceDistance còn thấp thì càng giống
# =============================================================================

faceDistance = face_recognition.face_distance([encodeMailan], encodeUnknowImg)
print('faceDistance (sai số): ', faceDistance, type(faceDistance)) # ndarray
print(f'faceDistance (sai số - quy đổi theo thang 100%): {faceDistance * 100}%')


# =============================================================================
# add faceDistance to image => unknown image 
# =============================================================================

# vì faceDistance là array => cần index | faceDistance[0] 
# dùng round() làm tròn 2 số => round(faceDistance[0], 2)
resultTextOfImage = f'{imgResult} - {round(faceDistance[0], 2)*100}%' # ra sai số

# chuyển từ sai số qua tỷ lệ % giống nhau (1 - sai số) | => độ tin cậy | Confidence interval
resultTextOfImageConfidenceInterval = f'{imgResult} - {round((1 - faceDistance[0]) * 100, 2)}%' # ra dộ tin cậy



print('resultTextOfImage: ', resultTextOfImage)
print('resultTextOfImageConfidenceInterval: ', resultTextOfImageConfidenceInterval)

# add text | sai số
# cv2.putText(unknownImg, resultTextOfImage, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, .8, (0, 255, 0), 2)

# add text | độ tin cậy
cv2.putText(unknownImg, resultTextOfImageConfidenceInterval, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, .8, (0, 255, 0), 2)
    

# =============================================================================
# Show image
# =============================================================================

# CASE 1 - show image 1 by 1
# cv2.imshow('Do Mai Lan', imgMaiLan)
# cv2.imshow('Unknown Image', unknownImg)

# CASE 2 - show both image in a window
# Concatenate the images horizontally
concatenated_img = cv2.hconcat([imgMaiLan, unknownImg])

# Display the concatenated image in a window
cv2.imshow("Two images in one window", concatenated_img)
cv2.waitKey()

cv2.destroyAllWindows()
print('finished')





















