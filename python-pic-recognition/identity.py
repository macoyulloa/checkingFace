import face_recognition
from PIL import Image, ImageDraw

image_of_steve = face_recognition.load_image_file('./img/known/steve-jobs.jpeg')
steve_face_encoding = face_recognition.face_encodings(image_of_steve)[0]

know_face_encodings = [
    steve_face_encoding
]

know_face_names = [
    "Steve Jobs"
]

test_image = face_recognition.load_image_file('./img/groups/bill-steve-group.jpeg')

#find faces
face_locations = face_recognition.face_locations(test_image)
print(len(face_locations))
face_encodings = face_recognition.face_encodings(test_image, face_locations)

pil_image = Image.fromarray(test_image)

draw = ImageDraw.Draw(pil_image)

for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(know_face_encodings, face_encoding)
    name = "Unknow Person"

    if True in matches:
        first_match_index = matches.index(True)
        name = know_face_names[first_match_index]

    # draw
    draw.rectangle(((left, top), (right, bottom)) , outline=(0,0,0))
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0),outline=(0,0,0))
    draw.text((left + 6, bottom - text_height -5), name, fill=(255,255,255,255))

del draw

pil_image.show()
# pil_image.save('./')

