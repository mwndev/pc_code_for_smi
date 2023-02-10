import cv2
from matplotlib import pyplot as plt
import time
import os
# cap = cv2.VideoCapture('/dev/video2')

# ret, frame = cap.read()

# print(frame)

# plt.imshow(frame)


# def take_photo():
#     cap = cv2.VideoCapture('/dev/video2')
#     ret, frame = cap.read()
#     print(frame)
#     cv2.imwrite('wevcc.jpg', frame)
#     cap.release()
# take_photo()

cap = cv2.VideoCapture('/dev/video2')
# print("w" + cap.width)
# print("h" + cap.height)
while cap.isOpened():
    ret, frame = cap.read()
    print(len(frame[1]))
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(1)
print('end')
cap.release()
