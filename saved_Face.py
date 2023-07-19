import face_recognition
import pickle

# Global variable to store the face encodings of known profiles
known_encodings = []

# Load the known profiles and their corresponding face images
known_profiles = {
    "Main user": "face/face.jpg",
    # Add more known profiles as needed
}

# Load and encode the known profiles
for profile_path in known_profiles.values():
    profile_image = face_recognition.load_image_file(profile_path)
    profile_encoding = face_recognition.face_encodings(profile_image)[0]
    known_encodings.append(profile_encoding)

# Save the known encodings to a file using pickle
with open("known_encodings.pkl", "wb") as f:
    pickle.dump(known_encodings, f)

with open("known_encodings.pkl", "rb") as f:
    known_encodings = pickle.load(f)
    print(known_encodings)
