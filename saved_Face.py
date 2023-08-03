# import face_recognition
# import pickle
# import os, time, uuid, cv2
#
# # Global variable to store the face encodings of known profiles
# known_profiles = []
#
# # Load the known profiles and their corresponding face images
# known_profiles_info = [
#     {
#         "name": "Main user",
#         "paths": ["face/faceV2.jpg", "face/face.jpg", "face/faceV3.jpg"]
#     },
#     {
#         "name": "elon musk",
#         "paths": ["face/elonmusk.jpg", "face/elonmusk2.jpg"]
#     },
#     # Add more known profiles as needed
# ]
#
# # Load and encode the known profiles
# for profile_info in known_profiles_info:
#     face_encodings = []
#     for profile_path in profile_info["paths"]:
#         profile_image = face_recognition.load_image_file(profile_path)
#         profile_encoding = face_recognition.face_encodings(profile_image)[0]
#         face_encodings.append(profile_encoding)
#     known_profiles.append({
#         "name": profile_info["name"],
#         "encodings": face_encodings
#     })
#
# # Save the known profiles to a file using pickle
# with open("known_profiles.pkl", "wb") as f:
#     pickle.dump(known_profiles, f)


import face_recognition
import pickle

# Global variable to store the face encodings of known profiles
known_encodings = []

# Load the known profiles and their corresponding face images

known_profiles_info = [
    {"name": "main user", "path": "face/face.jpg"},
    {"name": "elon musk", "path": "face/elonmusk.jpg"},
    # Add more known profiles as needed
]

# Load and encode the known profiles
for profile in known_profiles_info:
    profile_image = face_recognition.load_image_file(profile["path"])
    profile_encoding = face_recognition.face_encodings(profile_image)[0]
    known_encodings.append(profile_encoding)

# Save the known encodings to a file using pickle
with open("known_encodings.pkl", "wb") as f:
    pickle.dump(known_encodings, f)
