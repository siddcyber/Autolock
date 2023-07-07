from tkinter import *
import cv2
from PIL import Image, ImageTk

# Function to start video playback
def start_video():
    global capture, cameraCanvas, stop_video
    capture = cv2.VideoCapture(0)
    stop_video = False
    play_video()

# Function to stop video playback
def stop_video():
    global stop_video
    stop_video = True
    capture.release()

# Function to continuously play video frames
def play_video():
    global capture, cameraCanvas, stop_video
    if not stop_video:
        ret, frame = capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            frame = ImageTk.PhotoImage(image=frame)
            cameraCanvas.create_image(0, 0, image=frame)
            cameraCanvas.image = frame  # Store a reference to prevent garbage collection
        cameraCanvas.after(15, play_video)  # Call the play_video() function again after a delay

# Create the Tkinter window
root = Tk()
root.geometry("700x360")
root.configure(background="White")
root.title("Face Recognition Autolock")

# Create a frame for buttons
optionFrame = LabelFrame(root, background='white')
optionFrame.grid(row=1, column=0, sticky='NSEW', columnspan=2)

# Button to start video playback
startButton = Button(optionFrame, text='Start', command=start_video, background='White')
startButton.grid(row=0, column=0, sticky='EW')

# Button to stop video playback
stopButton = Button(optionFrame, text='Stop', command=stop_video, background='White')
stopButton.grid(row=0, column=1, sticky='EW')

# Create a frame for camera display
cameraFrame = LabelFrame(root, background='White')
cameraFrame.grid(row=2, column=0, sticky='NSEW')

# Create a canvas for displaying video frames
cameraCanvas = Canvas(cameraFrame, width=700 // 2, height=360 // 2)
cameraCanvas.grid(row=0, column=0, sticky='NSEW')

# Run the Tkinter event loop
root.mainloop()


# from tkinter import *
# import cv2
# from PIL import Image, ImageTk
#
#
# # function for button to work -> check if startup is enable/disabled
# def checkstartup():
#     return True
#
#
# # function for button to work -> check to enable camera or not
# def checkCamera():
#     return True
#
#
# # function for button to work -> button to change log location
# def changelog():
#     return True
#
#
# def startORstop():
#     return True
#
#
# def videoPlayer():
#     ret, frame = capture.read()
#     if ret:
#         frame = cv2.cvtColor(capture.read()[1], cv2.COLOR_BGR2RGB)
#         frame = Image.fromarray(frame)
#         frame = ImageTk.PhotoImage(image=frame)
#         # cameraCanvas.configure(image=frame)
#         cameraCanvas.create_image(0, 0, image=frame)
#     cameraCanvas.after(15, videoPlayer)
#
#
# # main window initialization and properties
# window = Tk()
# window.geometry("700x360")
# window.configure(background="White")
# window.title("Face Recognition Autolock")
# heading = Label(window, text="Face Recognition Autolock", relief='raised', bg="White")
# capture = cv2.VideoCapture(0)
#
# # first frame for buttons
# optionFrame = LabelFrame(window, background='white')
# startupButton = Button(optionFrame, text='Startup', command=checkstartup, background='White')
# showCameraButton = Button(optionFrame, text='Show camera', command=checkCamera, background='White')
# changelogLoc = Button(optionFrame, text='Change log location', command=changelog, background='White')
#
# # second frame for camera and related
# cameraFrame = LabelFrame(window, background='White')
# cameraCanvas = Canvas(cameraFrame, width=700 // 2, height=360 // 2)
# cameralabel = Label(cameraFrame, relief='raised', text="no face detected", background='White')
#
# #  third frame for log and start/stop button
# logFrame = LabelFrame(window, background='White')
# log = Listbox(logFrame, background='White')
# log.insert(0, "log")
# startStopButton = Button(logFrame, text='Start', command=startORstop, background='White')
#
# # code for creating a dynamic size window
# window.rowconfigure(index=2, weight=1)
# window.columnconfigure(index=0, weight=1)
# optionFrame.columnconfigure(index=0, weight=1)
# optionFrame.columnconfigure(index=1, weight=1)
# optionFrame.columnconfigure(index=2, weight=1)
# cameraFrame.columnconfigure(index=0, weight=1)
# cameraFrame.columnconfigure(index=1, weight=1)
# cameraFrame.rowconfigure(index=0, weight=1)
# cameraFrame.rowconfigure(index=1, weight=1)
# logFrame.columnconfigure(index=0, weight=1)
# logFrame.columnconfigure(index=1, weight=1)
# logFrame.rowconfigure(index=0, weight=1)
# logFrame.rowconfigure(index=1, weight=1)
#
# # putting all widgets to grid
# heading.grid(row=0, column=0, sticky='NSEW', columnspan=2)
# optionFrame.grid(row=1, column=0, sticky='NSEW', columnspan=2)
# startupButton.grid(row=0, column=0, sticky='EW')
# showCameraButton.grid(row=0, column=1, sticky='EW')
# changelogLoc.grid(row=0, column=2, sticky='EW')
# cameraFrame.grid(row=2, column=0, sticky='NSEW')
# cameraCanvas.grid(row=0, column=0, sticky='NSEW')
# cameralabel.grid(row=1, column=0, sticky='EW')
# logFrame.grid(row=2, column=1, sticky='NSEW')
# log.grid(row=0, column=0, sticky='NSEW')
# startStopButton.grid(row=1, column=0, sticky='EW')
#
# #  tkinter main loop
# window.mainloop()
# capture.release()
