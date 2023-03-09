# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 00:23:56 2023

@author: Admin
"""


import face_recognition

# Load the known images
image_of_person_1 = face_recognition.load_image_file("img/person_1.jpg")
image_of_person_2 = face_recognition.load_image_file("img/person_2.jpg")
image_of_person_3 = face_recognition.load_image_file("img/person_3.jpg")

# Get the face encodings for each person. This can take some time for large images.
person_1_face_encoding = face_recognition.face_encodings(image_of_person_1)[0]
person_2_face_encoding = face_recognition.face_encodings(image_of_person_2)[0]
person_3_face_encoding = face_recognition.face_encodings(image_of_person_3)[0]

# Create a list of known face encodings
known_face_encodings = [
    person_1_face_encoding,
    person_2_face_encoding,
    person_3_face_encoding
]

# Load the image we want to check
unknown_image = face_recognition.load_image_file("img/unknown2.jpg")

# Get face encodings for any faces in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
unknown_face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Loop through the faces in the unknown image
for unknown_face_encoding in unknown_face_encodings:
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)

    # If a match was found in the known_face_encodings list, print the name
    if True in matches:
        first_match_index = matches.index(True)
        name = "Person " + str(first_match_index + 1)
        print(f"Found {name} in the photo!")
    else:
        print("Unknown person found in the photo!")

