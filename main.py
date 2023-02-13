import cv2
from matplotlib import pyplot as plt
import time
import os
from pymongo import MongoClient


mongLink = os.getenv("MONGO_URI")


cap = cv2.VideoCapture('/dev/video2')


while cap.isOpened():
    ret, frame = cap.read()
    print(len(frame[1]))
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(1)
print('end')
cap.release()
