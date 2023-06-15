import tkinter, time, os, threading, sys, math, datetime
import face_recognition
import cv2
import cmake
import numpy as np
import dlib
# import pyautogui
# from pynput import keyboard, mouse
# import pygetwindow as gw

#  input still provided( try other methods)
# check for platform specific controls
#  check if gpu acceleration works
print(cv2.cuda.getCudaEnabledDeviceCount())
# def disable_input():
#     # Get the active window handle
#     active_window = gw.getActiveWindow()
#
#     # Block keyboard and mouse input for the active window
#     active_window.block_input()
#
#     # Wait for the specified duration
#     time.sleep(100)
#
#     # Unblock keyboard and mouse input for the active window
#     active_window.unblock_input()
#
#     # Print a message indicating that input is re-enabled
#     print("Keyboard and mouse input enabled.")
#
# # Call the function to disable input for 100 seconds
# print("Disabling keyboard and mouse input for 100 seconds...")
# disable_input()

# def disable_input():
#     # Disable keyboard and mouse input
#     pyautogui.FAILSAFE = False
#     pyautogui.mouseDown()
#     pyautogui.mouseUp()
#     pyautogui.typewrite('')
#
#     # Wait for the specified duration
#     time.sleep(100)
#
#     # Re-enable keyboard and mouse input
#     pyautogui.FAILSAFE = True
#
#     # Print a message indicating that input is re-enabledable
#     print("Keyboard and mouse input enabled.")
#
# # Call the function to disable input for 100 seconds
# print("Disabling keyboard and mouse input for 100 seconds...")
# disable_input()

# # Create keyboard and mouse controllers
# keyboard_controller = keyboard.Controller()
# mouse_controller = mouse.Controller()
#
# # Disable keyboard and mouse input
# keyboard_controller.release(keyboard.Key.alt)  # Release any modifier keys if pressed
# keyboard_controller.release(keyboard.Key.shift)
# keyboard_controller.release(keyboard.Key.ctrl)
# keyboard_controller.release(keyboard.Key.cmd)
# mouse_controller.position = (0, 0)  # Move mouse to an arbitrary position
#
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
