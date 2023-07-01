import cv2
import threading

# loading haar cascades profiles( using hardocded locations )
face_cascade = cv2.CascadeClassifier(
    'C:\Program Files\Python39\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
profile_cascade = cv2.CascadeClassifier(
    'C:\Program Files\Python39\Lib\site-packages\cv2\data\haarcascade_profileface.xml')

