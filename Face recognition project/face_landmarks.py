import face_recognition
import PIL.ImageDraw
import PIL.Image
#loading the image as an array
image = face_recognition.load_image_file('sample.jpg')

#finding all face landmarks
face_landmarks_list = face_recognition.face_landmarks(image)


number_of_faces = len(face_landmarks_list)
print("I found {} face(s) in the picture".format(number_of_faces))

#load the image into python image library object
pil_image = PIL.Image.fromarray(image)

#creating object of PIL Image Draw
draw = PIL.ImageDraw.Draw(pil_image)

for face_landmarks in face_landmarks_list:
    #looping over each facial feature
    #print(face_landmarks)
    for name, list_of_points in face_landmarks.items():
        draw.line(list_of_points, fill= 'yellow', width = 2)

pil_image.show()