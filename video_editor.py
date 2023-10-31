import cv2
import os

video = cv2.VideoCapture('./bad_apple.mp4')

_, frame = video.read()

count = 0
SIZE = (100,100)
while _:
    os.system('cls')
    print(count)
    _, frame = video.read()
    resized_frame = cv2.resize(frame, SIZE)
    resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    (thresh, resized_frame) = cv2.threshold(resized_frame, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite('./frames/frame%d.jpg' % count, resized_frame)
    if cv2.waitKey(10) == 27:
        break
    count += 1

