import face_recognition
import cv2
import os
import pickle

from face_recognition.api import face_encodings
print(cv2.__version__)

Encodings = []
Names = []

image_dir = '/home/abdallah/Desktop/pyPro/faceRecognizer/companyImages/known'
for root, dirs, files in os.walk(image_dir): # walks through all the files and directories
    #print(files)
    for file in files:
        path = os.path.join(root,file)
        #print(path)
        name = os.path.splitext(file)[0]
        #print(name)
        person = face_recognition.load_image_file(path)
        encoding = face_recognition.face_encodings(person)[0] # returns an array but we choose the first
        Encodings.append(encoding)
        Names.append(name)

print(Names) # print encoded names to double check

# lets save the training data
# train.pkl : is the name of file we create
# wb : stands for write bites
# f : is the file we interact with when we write/read to/from a file
with open('company3.pkl', 'wb') as f:
    pickle.dump(Names,f) # save the learnt Names in f
    pickle.dump(Encodings,f) # save the learnt Encodings in f
