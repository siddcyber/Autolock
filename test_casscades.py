import os, threading, sys, math, datetime
from time import sleep, time
import cv2
import face_recognition
import pickle
import tkinter as tk
from tkinter import *
import cmake
import numpy as np
import dlib

start = time()
# finally a code that works
# must be implemented using admin rights
# from ctypes import windll
#
# windll.user32.BlockInput(True)  # this will block the keyboard input
# print("started")
# for i in range(10):
#     sleep(1) # input will be blocked for 15 seconds
#     print(i)
# windll.user32.BlockInput(False)  # now the keyboard will be unblocked
# print("ended")

# haar cascades for face recognition
# starting video capture
capture = cv2.VideoCapture(0)
# loading haar cascades profiles( using hardocded locations )
face_cascade = cv2.CascadeClassifier(
    'C:\Program Files\Python39\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
profile_cascade = cv2.CascadeClassifier(
    'C:\Program Files\Python39\Lib\site-packages\cv2\data\haarcascade_profileface.xml')

userImage = face_recognition.load_image_file("face/face.jpg")
knownFace = face_recognition.face_encodings(userImage, model="small")[0]

# with open("known_encodings.pkl", "rb") as f:
#     knownFace = pickle.load(f)
#     print(knownFace)

faceNames = []

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
        extracted_face = frame[y:y + height, x:x + width]
        # extracted_face = cv2.cvtColor(frame[y:y + height, x:x + width], cv2.COLOR_GRAY2RGB)
        # use face recognition library here for face recognition and further processing
        RGB = cv2.cvtColor(extracted_face, cv2.COLOR_BGR2RGB)
        # face_encodings = face_recognition.face_encodings(RGB)
        # for face_encoding in face_encodings:
        #     # Compare the detected face encoding with known encodings
        #     matches = face_recognition.compare_faces(knownFace, face_encoding, tolerance=0.5)
        #
        #     for i, match in enumerate(matches):
        #         if match:
        #             # Get the name of the matched profile
        #             profile_name = known_profiles[i]["name"]
        #             print(f"Detected profile: {profile_name}")
        face_encodings = face_recognition.face_encodings(RGB)
        for currentFace in face_encodings:
            matches = face_recognition.compare_faces([knownFace], currentFace)
            if any(matches):
                print("user")
            else:
                print("Unknown")


    # code to check if profile was detected and print detected time
    if len(profiles) > 0 or len(profiles_flip) > 0:
        currentTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print("profile found", currentTime)

    # drawing rectangles for profiles right
    for (x, y, width, height) in profiles:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
        print("right:", x, y, width, height)
    # drawing rectangles for profiles left
    for (x, y, width, height) in profiles_flip:
        cv2.rectangle(frame, (width - 1 - x, y) , (x + width, y + height), (0, 255, 0), 2)
        print("left:", width - 1 - x, y, width, height)

    # # get dimensions of frame
    # dimensions = frame.shape
    # # height, width, number of channels of frame
    # height = frame.shape[0]
    # width = frame.shape[1]
    # channels = frame.shape[2]
    # print('Image Dimension    : ', dimensions)
    # print('Image Height       : ', height)
    # print('Image Width        : ', width)
    # print('Number of Channels : ', channels)

    # displaying the frame
    cv2.imshow('frame', frame)
    # break code when q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    sleep(10)
    break
# closing the window and releasing the camera
capture.release()
cv2.destroyAllWindows()
end = time()
print(end - start)