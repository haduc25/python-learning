import cv2 as cv
capture = cv.VideoCapture(0)  # Nếu có nhiều webcam thì id 1, 2, 3...


"""_summary_
    cv.VideoCapture(0)  # Nếu có nhiều webcam thì id 1, 2, 3...
    cv.VideoCapture(video.mp4)  # Dùng video
    cv.VideoCapture(pathVideo)
    """

# Cho chụp ảnh liên tục
while True:
    ret, frame = capture.read()  # đọc img & chuyển về ret, frame
    print(ret)

    # show img
    cv.imshow('My Capture', frame)

    # waiting key / 1s
    if (cv.waitKey(1) == ord('q')):
        break

# exit camera
capture.release()

# close window
cv.destroyAllWindows()

"""_summary_
ret: return true/false
    - true: quá trình chụp ảnh diễn ra ok
    - false: khi camera bị chiếm dụng bởi phần mềm khác
"""
