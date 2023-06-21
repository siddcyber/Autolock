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
# starting video capture
capture = cv2.VideoCapture(0)
# loading haar cascades profiles( using hardocded locations )
face_cascade = cv2.CascadeClassifier(
    'C:\Program Files\Python39\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
profile_cascade = cv2.CascadeClassifier(
    'C:\Program Files\Python39\Lib\site-packages\cv2\data\haarcascade_profileface.xml')

while True:
    _, frame = capture.read()
    # converting frame to grayscale for analysis
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # flipping the grayscale for left side analysis for haarcascade_profileface
    gray_flip = cv2.flip(gray, 1)
    # detecting faces
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    # detecting profiles right
    profiles = profile_cascade.detectMultiScale(gray, 1.2, 5)
    # detecting profiles left
    profiles_flip = profile_cascade.detectMultiScale(gray_flip, 1.2, 5)
    ## drawing rectangles
    # drawing rectangles for face
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 2)
    # drawing rectangles for profiles right
    # if len(profiles) > 0 or len(profiles_flip) > 0:
    for (x, y, width, height) in profiles:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
        print("right:", x, y, width, height)
    # drawing rectangles for profiles left
    for (x, y, width, height) in profiles_flip:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
        print("left:", x, y, width, height)

    # displaying the frame
    cv2.imshow('frame', frame)
    # break code when q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# closing the window and releasing the camera
capture.release()
cv2.destroyAllWindows()
