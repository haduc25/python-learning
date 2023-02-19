import cv2 as cv

"""_summary_
    imread(pathname, flag)
    flag: 
        1: trả về ảnh màu, bỏ qua Alpha (độ trong suốt)  
        0: trả về ảnh đen trắng
        -1: trả về ảnh màu, có Alpha (độ trong suốt)  
    
    cv.imshow(winname, mat)
    cv.imshow('My image', img)
    """

# reading image
img = cv.imread('D:\Coding\Python\Learning\Self\opencv\img\love.jpg', 1)

# show image
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.resizeWindow('image', 440, 700)
cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()
