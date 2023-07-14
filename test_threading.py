import cv2
import threading
#
# # loading haar cascades profiles( using hardocded locations )
# face_cascade = cv2.CascadeClassifier(
#     'C:\Program Files\Python39\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
# profile_cascade = cv2.CascadeClassifier(
#     'C:\Program Files\Python39\Lib\site-packages\cv2\data\haarcascade_profileface.xml')
#
# # importing required libraries
# import cv2
# import time
# from threading import Thread  # library for implementing multi-threaded processing
#
#
# # defining a helper class for implementing multi-threaded processing
# class WebcamStream:
#     def __init__(self, stream_id=0):
#         self.stream_id = stream_id  # default is 0 for primary camera
#
#         # opening video capture stream
#         self.vcap = cv2.VideoCapture(self.stream_id)
#         if self.vcap.isOpened() is False:
#             print("[Exiting]: Error accessing webcam stream.")
#             exit(0)
#         fps_input_stream = int(self.vcap.get(5))
#         print("FPS of webcam hardware/input stream: {}".format(fps_input_stream))
#
#         # reading a single frame from vcap stream for initializing
#         self.grabbed, self.frame = self.vcap.read()
#         if self.grabbed is False:
#             print('[Exiting] No more frames to read')
#             exit(0)
#
#         # self.stopped is set to False when frames are being read from self.vcap stream
#         self.stopped = True
#
#         # reference to the thread for reading next available frame from input stream
#         self.t = Thread(target=self.update, args=())
#         self.t.daemon = True  # daemon threads keep running in the background while the program is executing
#
#     # method for starting the thread for grabbing next available frame in input stream
#     def start(self):
#         self.stopped = False
#         self.t.start()
#
#         # method for reading next frame
#
#     def update(self):
#         while True:
#             if self.stopped is True:
#                 break
#             self.grabbed, self.frame = self.vcap.read()
#             if self.grabbed is False:
#                 print('[Exiting] No more frames to read')
#                 self.stopped = True
#                 break
#         self.vcap.release()
#
#     # method for returning latest read frame
#     def read(self):
#         return self.frame
#
#     # method called to stop reading frames
#     def stop(self):
#         self.stopped = True
#
#     # initializing and starting multi-threaded webcam capture input stream
#
#
# webcam_stream = WebcamStream(stream_id=0)  # stream_id = 0 is for primary camera
# webcam_stream.start()
#
# # processing frames in input stream
# num_frames_processed = 0
# start = time.time()
# while True:
#     if webcam_stream.stopped is True:
#         break
#     else:
#         frame = webcam_stream.read()
#
#         # adding a delay for simulating time taken for processing a frame
#     delay = 0.03  # delay value in seconds. so, delay=1 is equivalent to 1 second
#     time.sleep(delay)
#     num_frames_processed += 1
#
#     cv2.imshow('frame', frame)
#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break
# end = time.time()
# webcam_stream.stop()  # stop the webcam stream
#
# # printing time elapsed and fps
# elapsed = end - start
# fps = num_frames_processed / elapsed
# print("FPS: {} , Elapsed Time: {} , Frames Processed: {}".format(fps, elapsed, num_frames_processed))
#
# # closing all windows
# cv2.destroyAllWindows()
# import datetime
# class FPS:
#     def __init__(self):
#         # store the start time, end time, and total number of frames
#         # that were examined between the start and end intervals
#         self._start = None
#         self._end = None
#         self._numFrames = 0
#
#     def start(self):
#         # start the timer
#         self._start = datetime.datetime.now()
#         return self
#
#     def stop(self):
#         # stop the timer
#         self._end = datetime.datetime.now()
#
#     def update(self):
#         # increment the total number of frames examined during the
#         # start and end intervals
#         self._numFrames += 1
#
#     def elapsed(self):
#         # return the total number of seconds between the start and
#         # end interval
#         return (self._end - self._start).total_seconds()
#
#     def fps(self):
#         # compute the (approximate) frames per second
#         return self._numFrames / self.elapsed()
#
#
# class WebcamVideoStream:
#     def __init__(self, src=0):
#         # initialize the video camera stream and read the first frame
#         # from the stream
#         self.stream = cv2.VideoCapture(src)
#         (self.grabbed, self.frame) = self.stream.read()
#         # initialize the variable used to indicate if the thread should
#         # be stopped
#         self.stopped = False
#
#         def start(self):
#             # start the thread to read frames from the video stream
#             threading.Thread(target=self.update, args=()).start()
#             return self
#
#         def update(self):
#             # keep looping infinitely until the thread is stopped
#             while True:
#                 # if the thread indicator variable is set, stop the thread
#                 if self.stopped:
#                     return
#                 # otherwise, read the next frame from the stream
#                 (self.grabbed, self.frame) = self.stream.read()
#
#         def read(self):
#             # return the frame most recently read
#             return self.frame
#
#         def stop(self):
#             # indicate that the thread should be stopped
#             self.stopped = True
#
#
# from imutils.video import WebcamVideoStream
# from imutils.video import FPS
# import argparse
# import imutils
#
# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-n", "--num-frames", type=int, default=100,
#                 help="# of frames to loop over for FPS test")
# ap.add_argument("-d", "--display", type=int, default=1,
#                 help="Whether or not frames should be displayed")
# args = vars(ap.parse_args())
# # grab a pointer to the video stream and initialize the FPS counter
# print("[INFO] sampling frames from webcam...")
# stream = cv2.VideoCapture(0)
# fps = FPS().start()
# # loop over some frames
# while fps._numFrames < args["num_frames"]:
#     # grab the frame from the stream and resize it to have a maximum
#     # width of 400 pixels
#     (grabbed, frame) = stream.read()
#     frame = imutils.resize(frame, width=400)
#     # check to see if the frame should be displayed to our screen
#     if args["display"] > 0:
#         cv2.imshow("Frame", frame)
#         key = cv2.waitKey(1) & 0xFF
#     # update the FPS counter
#     fps.update()
# # stop the timer and display FPS information
# fps.stop()
# print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
# print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
# # do a bit of cleanup
# stream.release()
# cv2.destroyAllWindows()
# # created a *threaded* video stream, allow the camera sensor to warmup,
# # and start the FPS counter
# print("[INFO] sampling THREADED frames from webcam...")
# vs = WebcamVideoStream(src=0).start()
# fps = FPS().start()
# # loop over some frames...this time using the threaded stream
# while fps._numFrames < args["num_frames"]:
#     # grab the frame from the threaded video stream and resize it
#     # to have a maximum width of 400 pixels
#     frame = vs.read()
#     frame = imutils.resize(frame, width=400)
#     # check to see if the frame should be displayed to our screen
#     if args["display"] > 0:
#         cv2.imshow("Frame", frame)
#         key = cv2.waitKey(1) & 0xFF
#     # update the FPS counter
#     fps.update()
# # stop the timer and display FPS information
# fps.stop()
# print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
# print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
# # do a bit of cleanup
# cv2.destroyAllWindows()
# vs.stop()

import cv2
import face_recognition
import threading

# Global variable to store the face encodings of known profiles
known_encodings = []

# Load the known profiles and their corresponding face images
known_profiles = {
    "person1": "path/to/person1_profile.jpg",
    "person2": "path/to/person2_profile.jpg",
    # Add more known profiles as needed
}

# Load and encode the known profiles
for profile_path in known_profiles.values():
    profile_image = face_recognition.load_image_file(profile_path)
    profile_encoding = face_recognition.face_encodings(profile_image)[0]
    known_encodings.append(profile_encoding)


# Function to continuously extract frames from video capture
def extract_frames(video_capture):
    while True:
        ret, frame = video_capture.read()

        # Process the frame as needed
        # ...

        # Display the frame or perform other operations
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()


# Function to perform face recognition using compare_faces
def perform_face_recognition(frame):
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        # Compare the detected face encoding with known encodings
        matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.5)

        if any(matches):
            # Get the indices of matched known profiles
            matched_indices = [i for i, match in enumerate(matches) if match]
            matched_profiles = [list(known_profiles.keys())[i] for i in matched_indices]

            # Process the matched profiles
            for profile in matched_profiles:
                print(f"Detected profile: {profile}")


# Create a VideoCapture object to capture video from the default webcam
video_capture = cv2.VideoCapture(0)

# Create and start the frame extraction thread
frame_thread = threading.Thread(target=extract_frames, args=(video_capture,))
frame_thread.start()

while True:
    ret, frame = video_capture.read()

    # Create and start a face recognition thread for each frame
    recognition_thread = threading.Thread(target=perform_face_recognition, args=(frame,))
    recognition_thread.start()

    # Continue with other processing in the main thread
    # ...

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
