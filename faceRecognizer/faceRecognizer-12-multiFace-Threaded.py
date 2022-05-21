import face_recognition
from threading import Thread
import cv2
import time
import numpy as np
import pickle

dtavg = 0
fps = 0
font = cv2.FONT_HERSHEY_SIMPLEX

Names = []
Encodings = []

with open('company3.pkl', 'rb') as f:
    Names = pickle.load(f)
    Encodings = pickle.load(f)

class vStream():
    def __init__(self, src, width, height, scaleFactor):
        self.width = width
        self.height = height
        self.scaleFactor = scaleFactor
        self.capture = cv2.VideoCapture(src)
        self.thread = Thread(target = self.update, args=())
        self.thread.daemon = True # tells the Thread to behave nicely with other threads
        self.thread.start()
    def update(self):
        while True: 
            _, self.frame = self.capture.read()
            self.frame2 = cv2.resize(self.frame, (self.width, self.height), fx=self.scaleFactor, fy=self.scaleFactor)
    def getFrame(self):
        return self.frame2

dispW = 320*1
dispH = 240*1
flip = 2 # or 2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam1 = vStream(0, dispW, dispH, 0.3)
#cam2 = vStream(camSet, dispW, dispH, 0.3)

startTime = time.time()

scaleFactor = 0.5

while True:
    try:
        myFrame1 = cam1.getFrame()
        cv2.rectangle(myFrame1, (0,0), (80,35), (0,0,255), 2)
        cv2.putText(myFrame1, 'webCam', (5,20), font, 0.5, (0,255,255), 1)
        cv2.rectangle(myFrame1, (0,35), (80,70), (0,0,255), -1)
        cv2.putText(myFrame1, str(round(fps,1)), (5,60), font, 0.5, (0,255,255), 1)
        #myFrame2 = cam2.getFrame()
        #cv2.rectangle(myFrame2, (0,0), (60,35), (0,0,255), 2)
        #cv2.putText(myFrame2, 'piCam', (5,20), font, 0.5, (0,255,255), 1)

        myFrame3 = np.hstack((myFrame1, myFrame1)) # horizontally stack

        frameRGB = cv2.cvtColor(myFrame3, cv2.COLOR_BGR2RGB)
        frameRGBSmall = cv2.resize(frameRGB, (0,0), fx = scaleFactor, fy = scaleFactor)
        facePositions = face_recognition.face_locations(frameRGBSmall)
        allEncodings = face_recognition.face_encodings(frameRGBSmall, facePositions)
        for (top, right, bottom , left), face_encoding in zip(facePositions, allEncodings):
            name = 'unknown Person'
            matches = face_recognition.compare_faces(Encodings, face_encoding)
            if True in matches:
                index = matches.index(True)
                name = Names[index]
            top = int(top/ scaleFactor)
            bottom = int(bottom / scaleFactor)
            right = int(right / scaleFactor)
            left = int(left / scaleFactor)
            cv2.rectangle(myFrame3, (left, top), (right, bottom), (0,0,255), 3)
            cv2.putText(myFrame3, name,(left, top-6), font, 0.75, (0,255,255), 2)

        dt = time.time() - startTime
        startTime = time.time()
        dtavg = 0.9*dtavg + 0.1*dt # low pass filter
        fps = 1/dtavg

        cv2.imshow('comboCam', myFrame3)
        cv2.moveWindow('comboCam', 0, 0)

    except:
        print('frame not available')
    if cv2.waitKey(1) == ord('q'):
        break

cam1.capture.release()
#cam2.capture.release()
cv2.destroyAllWindows()
exit(1)
