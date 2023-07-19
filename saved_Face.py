import cv2
import face_recognition
import threading
import pickle

# Global variable to store the face encodings of known profiles
known_encodings = []

# Load the known profiles and their corresponding face images
known_profiles = [
    {"name": "person1", "path": "path/to/person1_profile.jpg"},
    {"name": "person2", "path": "path/to/person2_profile.jpg"},
    # Add more known profiles as needed
]

# Load and encode the known profiles
for profile in known_profiles:
    profile_image = face_recognition.load_image_file(profile["path"])
    profile_encoding = face_recognition.face_encodings(profile_image)[0]
    known_encodings.append(profile_encoding)

# Save the known encodings to a file using pickle
with open("known_encodings.pkl", "wb") as f:
    pickle.dump(known_encodings, f)

#
# # Function to continuously extract frames from video capture
# def extract_frames(video_capture):
#     while True:
#         ret, frame = video_capture.read()
#
#         # Process the frame as needed
#         # ...
#
#         # Display the frame or perform other operations
#         cv2.imshow('Frame', frame)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     video_capture.release()
#
#
# # Function to perform face recognition using compare_faces
# def perform_face_recognition(frame):
#     # Convert the grayscale frame to RGB format
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
#
#     face_locations = face_recognition.face_locations(rgb_frame)
#     face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
#
#     for face_encoding in face_encodings:
#         # Compare the detected face encoding with known encodings
#         matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.5)
#
#         for i, match in enumerate(matches):
#             if match:
#                 # Get the name of the matched profile
#                 profile_name = known_profiles[i]["name"]
#                 print(f"Detected profile: {profile_name}")
#
#
# # Create a VideoCapture object to capture video from the default webcam
# video_capture = cv2.VideoCapture(0)
#
# # Create and start the frame extraction thread
# frame_thread = threading.Thread(target=extract_frames, args=(video_capture,))
# frame_thread.start()
#
# while True:
#     ret, frame = video_capture.read()
#
#     # Create and start a face recognition thread for each frame
#     recognition_thread = threading.Thread(target=perform_face_recognition, args=(frame,))
#     recognition_thread.start()
#
#     # Continue with other processing in the main thread
#     # ...
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# video_capture.release()
# cv2.destroyAllWindows()
