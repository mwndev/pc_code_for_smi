import cv2
from matplotlib import pyplot as plt
import time
import os
from pymongo import MongoClient
import generate_nn


mongLink = os.getenv("MONGO_URI")


cap = cv2.VideoCapture('/dev/video2')


while cap.isOpened():
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('webcam', gray_frame)
    fovea_frame = generate_nn.generate_fovea_array(gray_frame, 50)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('webcam', fovea_frame)
    time.sleep(0.05)
print('end')
cap.release()
