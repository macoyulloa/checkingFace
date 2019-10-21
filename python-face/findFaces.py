import face_recognition

image = face_recognition.load_image_file('./img/groups/group-faces.jpg')
# array of coord of each face
face_locations = face_recognition.face_locations(image)

print(face_locations)