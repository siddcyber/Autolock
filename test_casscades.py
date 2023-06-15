import tkinter, time, os, threading, sys, math, datetime
import face_recognition
import cv2
import cmake
import numpy as np
import dlib


# # Load the pre-trained face detection model
#
# # Set the threshold for face detection confidence
# face_confidence_threshold = 0.5
#
# # Set the maximum allowed consecutive frames without user presence
# max_inactive_frames = 30
#
# # Initialize variables
# inactive_frames = 0
# user_present = False
#
# # Disable keyboard and mouse
# pyautogui.FAILSAFE = False
# pyautogui.mouseDown()
# pyautogui.mouseUp()
# pyautogui.typewrite('')
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Failed to read frame from webcam")
#         break
#
#     # Perform face detection on the frame

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#
#     # Reset inactive frames counter if faces are detected
#     if len(faces) > 0:
#         inactive_frames = 0
#         user_present = True
#     else:
#         inactive_frames += 1
#
#     # Disable keyboard and mouse if user is not present
#     if not user_present and inactive_frames >= max_inactive_frames:
#         pyautogui.FAILSAFE = False
#         pyautogui.mouseDown()
#         pyautogui.mouseUp()
#         pyautogui.typewrite('')
#
#     # Enable keyboard and mouse if user is present
#     if user_present and inactive_frames == 0:
#         pyautogui.FAILSAFE = True
#
#     # Draw rectangles around the detected faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     # Display the frame
#     cv2.imshow("Webcam Feed", frame)
#
#     # Check for key press
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# # Release resources
# cap.release()
# cv2.destroyAllWindows()
