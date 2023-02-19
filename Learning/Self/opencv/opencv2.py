import cv2 as cv

# read img
img = cv.imread('Learning/Self/opencv/img/love.jpg', 1)
# img = cv.imread('Learning/Self/opencv/img/2.PNG', -1)

# resize img
# img = cv.resize(img, (0, 0), fx=.5, fy=.5)


# array of image
print(img)

# type of image
print(type(img))  # <class 'numpy.ndarray'>

# xem chieu cao => shape
print(img.shape)  # (741, 412, 3), Chiều cao => hàng & chiều rộng => cột

"""_summary_
    #########################
    print(img.shape) 
    # (741, 412, 3), Chiều cao => hàng & chiều rộng => cột
    741 - Chiều cao => hàng
    412 - chiều rộng => cột
    3 - kênh (chanel) => RGB, RGBA
    
    img = cv.imread('Learning/Self/opencv/img/love.jpg', 1) => chanel = RGB => 3
    img = cv.imread('Learning/Self/opencv/img/love.jpg', -1) => chanel = RGBA => 4
    """

################################################

# xuất dữ liệu của img theo index
print('#'*32)
# (1482, 824, 3)
print(img[0])  # value of index 0
print(img[1481])  # value of index 1481, because index from 0 - 1481


# show img
# cv.imshow('My Crush', img)

# stop window
# cv.waitKey()
