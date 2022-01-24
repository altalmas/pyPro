"""
To receive the udp stream :

gst-launch-1.0 udpsrc port=5000 ! \
application/x-rtp,encoding-name=H264,payload=96 ! \
rtph264depay ! \
h264parse ! \
queue ! \
avdec_h264 ! \
autovideosink sync=false async=false -e
"""

from threading import Thread
import cv2
import time
import numpy as np

class vStream():
    def __init__(self, src, width, height, scaleFactor):
        self.width = width
        self.height = height
        self.scaleFactor = scaleFactor
        self.capture = cv2.VideoCapture(src, cv2.CAP_GSTREAMER)
        self.thread = Thread(target = self.update, args=())
        self.thread.daemon = True # tells the Thread to behave nicely with other threads
        self.thread.start()

    def update(self):
        while True: 
            _, self.frame = self.capture.read()
            self.frame2 = cv2.resize(self.frame, (self.width, self.height), fx=self.scaleFactor, fy=self.scaleFactor)
    
    def getFrame(self):
        return self.frame2

dispW = 1280
dispH = 720
flip = 2 # or 2
camSet1='nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=60/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
out_pipeline = 'appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! video/x-raw, format=BGRx ! nvvidconv ! omxh264enc ! video/x-h264, stream-format=byte-stream ! h264parse ! rtph264pay pt=96 config-interval=1 ! udpsink host=192.168.178.63 port=5000'

cam1 = vStream(camSet1, dispW, dispH, 0.5) #Initialize Camera
out = cv2.VideoWriter(out_pipeline, 0, 60, (dispW,dispH)) # fps = 60

startTime = time.time()
font = cv2.FONT_HERSHEY_SIMPLEX
dtavg = 0
fps = 0

while True:
    try:
        myFrame1 = cam1.getFrame()
        cv2.rectangle(myFrame1, (0,0), (80,35), (0,0,255), 2)
        cv2.putText(myFrame1, 'piCam', (5,20), font, 0.5, (0,255,255), 1)
        cv2.rectangle(myFrame1, (0,35), (80,70), (0,0,255), -1)
        cv2.putText(myFrame1, str(round(fps,1)), (5,60), font, 0.5, (0,255,255), 1)

        cv2.imshow('piCam', myFrame1)
        cv2.moveWindow('piCam', 0, 0)

        out.write(myFrame1) # update the ouput stream pipeline

        dt = time.time() - startTime
        startTime = time.time()
        dtavg = 0.9*dtavg + 0.1*dt # low pass filter
        fps = 1/dtavg

    except:
        print('frame not available')

    if cv2.waitKey(1) == ord('q'):
        cam1.capture.release()
        cv2.destroyAllWindows()
        exit(1)
        #break

