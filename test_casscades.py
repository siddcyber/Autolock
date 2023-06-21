import tkinter, os, threading, sys, math, datetime
import cv2
import cmake
import numpy as np
import dlib

# finally a code that works
# must be implemented using admin rights
# from ctypes import windll
# from time import sleep
#
# windll.user32.BlockInput(True)  # this will block the keyboard input
# print("started")
# for i in range(10):
#     sleep(1) # input will be blocked for 15 seconds
#     print(i)
# windll.user32.BlockInput(False)  # now the keyboard will be unblocked
# print("ended")
#

# haar cascades for face recognition

capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('C:\Program Files\Python39\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
profile_cascade = cv2.CascadeClassifier('C:\Program Files\Python39\Lib\site-packages\cv2\data\haarcascade_profileface.xml')
while True:
    _, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 2)


    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()