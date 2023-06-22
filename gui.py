import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Create a tkinter window
window = tk.Tk()
window.title("Face Detection")

# Open the webcam
cap = cv2.VideoCapture(0)

# Load the pre-trained face detection cascade classifier
face_cascade = cv2.CascadeClassifier(
    'C:\Program Files\Python39\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
profile_cascade = cv2.CascadeClassifier(
    'C:\Program Files\Python39\Lib\site-packages\cv2\data\haarcascade_profileface.xml')

# Function to detect faces and display messagebox
def detect_faces():
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame using the cascade classifier
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Display the frame in the tkinter window
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    img = img.resize((400, 300))
    imgtk = ImageTk.PhotoImage(image=img)
    label.configure(image=imgtk)
    label.image = imgtk

    # Check if faces are detected
    if len(faces) > 0:
        messagebox.showinfo("Face Detected", "A face has been detected!")

    # Schedule the next detection
    window.after(10, detect_faces)

# Create a label to display the webcam feed
label = tk.Label(window)
label.pack()

# Start the face detection process
window.after(10, detect_faces)

# Start the tkinter event loop
window.mainloop()

# Release the webcam
cap.release()
