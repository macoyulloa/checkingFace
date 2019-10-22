import cv2
import face_recognition

# Get a reference to webcam
video_capture = cv2.VideoCapture("/dev/video0")


image = face_recognition.load_image_file("./data-images/andres.png")
face_encoding = face_recognition.face_encodings(image)[0]

known_faces = [
    face_encoding,
]

# Initialize variables
face_locations = []
face_encodings = []
face_names = [
    "andres"
]
frame_number = 0

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    frame_number += 1

    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color
    # (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame, model="cnn")
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(
            known_faces, face_encoding)

        name = "Unknow"
        if True in match:
            first_match_index = match.index(True)
            name = face_names[first_match_index]

    # Label the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 25),
                      (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 0.5, (255, 255, 255), 1)

    # Write the resulting image to the output video file
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
