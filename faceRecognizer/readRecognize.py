import face_recognition
import cv2
import os
import pickle

from face_recognition.api import face_encodings
print(cv2.__version__)

j = 0 # counter
Encodings = [] # begin fresh
Names = [] 

with open('train.pkl', 'rb') as f: # rb : stands from read bites
    Names = pickle.load(f) # get the data from f and put them in Names
    Encodings = pickle.load(f) # same


# ----- We have done the recognition part
# lets use any image to try on:
font = cv2.FONT_HERSHEY_SIMPLEX

image_dir = '/home/abdallah/Desktop/pyPro/faceRecognizer/demoImages/unknown'
for root, dir, files in os.walk(image_dir): # walk through all unknown files
    for file in files:
        print(root)
        print(file)
        testImagePath = os.path.join(root,file)
        testImage = face_recognition.load_image_file(testImagePath)
        facePositions = face_recognition.face_locations(testImage) # locate all faces on the image and put their positison in 1 array
        allEncodings = face_recognition.face_encodings(testImage,facePositions) # encode all the found faces
        testImage=cv2.cvtColor(testImage, cv2.COLOR_RGB2BGR) # we will work with cv2,  therefore we convert the pic to BGR

        #  (x1 , y1  , x2   , y2 ), # So, the coordinates are for the upper-right and lower-left corners of the face in face_recognition library
        for(top,right,bottom,left), face_encoding in zip(facePositions, allEncodings):
            name = 'Unknown Person'
            matches = face_recognition.compare_faces(Encodings,face_encoding)
            if True in matches:
                first_match_index = matches.index(True)
                name = Names[first_match_index]
            cv2.rectangle(testImage, (left,top), (right,bottom), (255,0,0), 2)
            cv2.putText(testImage, name, (left,top-6), font, 0.75, (0,255,255),2)

        cv2.imshow('pic', testImage)
        cv2.moveWindow('pic', 0, 0 )

        if cv2.waitKey(0) == ord('q'):
            cv2.destroyAllWindows()

