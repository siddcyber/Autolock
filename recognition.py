 # increase thread based on number of objects detected
import cv2


class recognition:
    def __init__(self,frame):
        self.rgb_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        self.known_face_encodings = []
