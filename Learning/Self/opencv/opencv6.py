import cv2 as cv
import os
import time

pTime = 0
capture = cv.VideoCapture(0)

# folder path
folderPath = 'Learning/Self/opencv/finger/imgFingers'

# read the folder
lst = os.listdir(folderPath)
lst_2 = []

# loop to get image in folder
for i in lst:
    # print(i)

    # Get source of image => Learning/Self/opencv/finger/imgFingers/1.png => 6.png
    print(f'{folderPath}/{i}')

    # add source to image
    image = cv.imread(f'{folderPath}/{i}')

    # add ma tran image va lst_2
    lst_2.append(image)

# checking length of array
print(len(lst_2))  # 6

# lay ra shape of image
print(lst_2[0].shape)  # (132, 109, 3)

print(lst)  # ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png']

while True:
    ret, frame = capture.read()

    # save value image[0] shape
    height, width, channel = lst_2[0].shape

    # show FPS | time.time() => trả về số giây, tính từ 0:0:00 ngày 1/1/1970 theo giờ UTC , gọi là (thời điểm bắt đầu thời gian)
    cTime = time.time()
    # 1 chia (thời gian hiện tại - thời gian ban đầu) | Tính FPS Frames per second - đây là  chỉ số khung hình trên mỗi giây
    fps = 1/(cTime-pTime)

    # gán lại để chạy lại vòng mới
    pTime = cTime

    print(fps)
    print(type(fps))  # float

    # display FPS on screen | putText
    cv.putText(frame, f'FPS: {int(fps)}', (150, 70),
               cv.FONT_HERSHEY_COMPLEX, 1.8, (0, 255, 0), 3)

    # gán dl vào frame / gán image vào frame
    frame[0:height, 0:width] = lst_2[0]  # (132, 109, 3)

    cv.imshow('Window capture', frame)

    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
