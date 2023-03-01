import cv2
from matplotlib import pyplot as plt
import time
import os
from pymongo import MongoClient
import generate_nn


mongLink = os.getenv("MONGO_URI")


cap = cv2.VideoCapture('/dev/video2')

frame_counter = 0


while cap.isOpened():
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if frame_counter is 0:
        # image where non-fovea is False, fovea is true
        fovea_array = generate_nn.generate_fovea_array(gray_frame, 50)
        layer_1 = generate_nn.generate_layer_1(
            fovea_array, fovea_density=2, fovea_connections=9, periph_density=0.25, periph_connections=3)

        layer_2 = generate_nn.generate_deep_layer(
            fovea_array, periph_proportion=0.25, fovea_proportion=4)
        print(len(layer_1))
        print(layer_1[30000])
        print(len(layer_2))
        print(layer_2[10000])

    # video feed BW
    cv2.imshow('webcam', gray_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.01)

    frame_counter += 1
print('end')
cap.release()
