import face_recognition
import PIL.Image
import PIL.ImageDraw

image = face_recognition.load_image_file('sample.jpg')  #converting image into numpy array
face_locations = face_recognition.face_locations(image)  #finding all faces

number_of_faces = len(face_locations)
print("Found {} faces in the picture".format(number_of_faces))
pil_image = PIL.Image.fromarray(image)   #loading image into python image lib object so that
                                         # we can draw on it and display it

for face_location in face_locations:
     top, right, bottom, left = face_location

     draw = PIL.ImageDraw.Draw(pil_image)
     draw.rectangle([left, top, right, bottom], outline = 'blue')

pil_image.show()