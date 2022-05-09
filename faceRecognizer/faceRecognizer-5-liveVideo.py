import face_recognition
import cv2
import os
import pickle
print(cv2.__version__)

Encodings = []
Names = []

with open('train.pkl', 'rb') as f:
    Names = pickle.load(f)
    Encodings = pickle.load(f)

dispW = 320*1
dispH = 240*1
flip = 2 # or 2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet) # Rasperri Pi Camera

cam = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    _, frame = cam.read()
    frameSmall = cv2.resize(frame, (0,0), fx = 0.33, fy=0.33) # resize to smaller for faster processing
    # remember that if you scale the frame down, the face will need to be bigger to recognize it in the camera, 
    # so there is a pay off between (how good and how fast the recognition is) > tune !

    frameRGB = cv2.cvtColor(frameSmall, cv2.COLOR_BGR2RGB) # the face_recognizer works in RGB
    facePositions = face_recognition.face_locations(frameRGB, model = 'cnn') # cnn is better (best face finder)
    allEncodings = face_recognition.face_encodings(frameRGB, facePositions)

    for (top,right, bottom, left), face_encoding in zip(facePositions, allEncodings):
        name = 'Unknown Person'
        matches = face_recognition.compare_faces(Encodings, face_encoding)
        if True in matches:
            first_match_index = matches(True)
            name = Names[first_match_index]
        top = top *3 # resize back to original
        right = right * 3
        left = left * 3
        bottom = bottom * 3
        cv2.rectangle(frame, (left, top), (right,bottom), (0,0,255),2)
        cv2.putText(frame, name, (left, top-6), font, 0.75, (0,255,255), 2)

    cv2.imshow('pic', frame)
    cv2.moveWindow('pic', 0, 0 )

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
