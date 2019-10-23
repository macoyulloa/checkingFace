import face_recognition
import cv2
from requests import get
import numpy as np
from skimage import io
import zlib


class VideoCamera(object):
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        # Create arrays of known face encodings and their names
        # Load a sample picture and learn how to recognize it.
        # Create arrays of known face encodings and their names
        self.known_face_encodings = []
        self.known_face_names = []

        # Load a sample picture and learn how to recognize it.
        images = []
        # Getting the images from the appi
        response = get('https://api-jwt-v3.herokuapp.com/api/all').json()
        for each in response:
            images.append(each['image_url'])
        # Saving the images in a numpy format, array
        for each_url_image in images:
            img = io.imread(each_url_image)
            face_encoding = face_recognition.face_encodings(img)[0]
            self.known_face_encodings.append(face_encoding)
        # Saving the names of the known people
        for each in response:
            self.known_face_names.append(each['name'])  

    def __del__(self):
        self.video.release()

    def get_frame(self):

        # Initialize some variables
        process_this_frame = True

        # Grab a single frame of video
        ret, frame = self.video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition
        # processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of
            # video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(
                    self.known_face_encodings, face_encoding, tolerance=0.5)
                name = "Unknown"

                if True in matches:
                    first_match_index = matches.index(True)
                    name = self.known_face_names[first_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (
                top, right, bottom, left), name in zip(
                face_locations, face_names):
            # Scale back up face locations since the frame we detected in was
            # scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        # Display the resulting image
        result, jpg = cv2.imencode('.jpg', frame, encode_param)

        return jpg.tobytes()
