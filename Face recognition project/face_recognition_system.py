import face_recognition as fr
import PIL.Image
import PIL.ImageDraw
# Load the known images
image1 = fr.load_image_file('person_1.jpg')
image2 = fr.load_image_file('person_2.jpg')
image3 = fr.load_image_file('person_3.jpg')

# Get the face encoding of each person. This can fail if no one is found in the photo.
face_encoding1 = fr.face_encodings(image1)[0]
face_encoding2 = fr.face_encodings(image2)[0]
face_encoding3 = fr.face_encodings(image3)[0]

# Create a list of all known face encodings
known_face_encodings = [
face_encoding1,
face_encoding2,
face_encoding3
]

# Load the image we want to check
unknown_image = fr.load_image_file('unknown_2.jpg')
# Get face encodings for any people in the picture
face_locations = fr.face_locations(unknown_image, number_of_times_to_upsample=2)
#number_of_times_to_upsample means
#How many times to upsample the image looking for faces. Higher numbers find smaller faces
unknown_face_encodings = fr.face_encodings(unknown_image, known_face_locations=face_locations)

# There might be more than one person in the photo, so we need to loop over each face we found
for unknown_face_encoding in unknown_face_encodings:
    # Test if this unknown face encoding matches any of the three people we know
    results = fr.compare_faces(known_face_encodings, unknown_face_encoding, tolerance= 0.6)

    name = 'Unknown'
    if results[0]:
        name = 'Person 1'
    elif results[1]:
        name = 'Person 2'
    elif results[2]:
        name = 'Person 3'
    if name != 'Unknown':
        print(f"Found {name} in the photo!")
    else:
        print("No person matches the unknown image")
        break
