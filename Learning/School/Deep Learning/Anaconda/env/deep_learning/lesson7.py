# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 10:36:04 2023

@author: Admin

[Nguồn tham khảo]
- https://huytranvan2010.github.io/Sliding-window-for-object-detection/
- https://pyimagesearch.com/2015/03/23/sliding-windows-for-object-detection-with-python-and-opencv/
"""
#imutils: a library for basic image processing tasks such as resizing and rotating images.
import cv2
import imutils
import time


# import the necessary packages
def pyramid(image, scale=1.5, minSize=(30, 30)):    # minSize là (width, height)
    # xuất ra ảnh gốc
    yield image 

    while True:
        # tính size mới và resize ảnh
        w = int(image.shape[1] / scale)     # thay đổi width này
        image = imutils.resize(image, width=w)

        # nếu kích thước ảnh nhỏ hơn minimum size yêu cầu (theo bất cứ chiều nào) thì dừng, thoát luôn
        if image.shape[0] < minSize[1] or image.shape[1] > minSize[0]:
            break 

        # xuất ra ảnh tiếp theo với size nhỏ hơn
        yield image

def sliding_window(image, stepSize, windowSize):    # windowSize = (width, height)
    # trượt các cửa sổ theo ảnh
    for y in range(0, image.shape[0], stepSize):    # duyệt theo hàng -  height
        for x in range(0, image.shape[1], stepSize):    # duyệt theo cột - width
            # xuất ra từng cửa sổ
            yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])   # có cả vị trí cho window và sliding window
            


######################################################
#                       MAIN                         #
######################################################

total_windows = 0

# Path to the image file
args = {"image": "../img/img2.jpg"}

image = cv2.imread(args["image"])
# Định nghĩa windowSize
(winW, winH) = (128, 128)

# Duyệt qua image pyramid
for resized in pyramid(image, scale=1.5):
    # Duyệt qua các sliding windows cho mỗi layer của image pyramid
    for (x, y, window) in sliding_window(image, stepSize=32, windowSize=(winW, winH)):
        # Nếu như window không thỏa mãn kích thước mong đợi của chúng ta thì bỏ qua
        if window.shape[0] != winH or window.shape[1] != winW:
            continue    # tiếp tục vòng lặp for
            # thực chất phần này sẽ dành cho việc khác
        
        clone = resized.copy()
        cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
        print(window.mean())
        cv2.imshow("window", clone)
        cv2.waitKey(1)
        time.sleep(0.025)
        
        # loading
        total_windows += 1
        progress_percent = total_windows * 100 / ((image.shape[0] - winH) * (image.shape[1] - winW))
        print(f"Progress: {progress_percent:.2f}%")


# end this
cv2.waitKey(0)
cv2.destroyAllWindows()













