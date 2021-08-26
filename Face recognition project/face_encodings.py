import face_recognition

# Load the jpg files into numpy arrays
image = face_recognition.load_image_file('people.jpg')

# Generate the face encodings
face_encodings = face_recognition.face_encodings(image)

if len(face_encodings) == 0:
    # No faces found in the image.
    print("No faces were found.")

else:
    # getting the first face encoding
    first_face_encoding = face_encodings[0]
    # Print the results
    print(len(face_encodings)) #number of people in the image
    print(first_face_encoding) #face encoding of the first person
