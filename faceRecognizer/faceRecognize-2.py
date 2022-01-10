import face_recognition
import cv2
print(cv2.__version__)

donFace = face_recognition.load_image_file('/home/abdallah/Desktop/pyPro/faceRecognizer/demoImages/known/Donald Trump.jpg')
donEncode = face_recognition.face_encodings(donFace)[0]

nancyFace = face_recognition.load_image_file('/home/abdallah/Desktop/pyPro/faceRecognizer/demoImages/known/Nancy Pelosi.jpg')
nancyEncode = face_recognition.face_encodings(nancyFace)[0]

