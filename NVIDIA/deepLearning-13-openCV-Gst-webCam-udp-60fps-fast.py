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
camSet2='v4l2src device=/dev/video1 ! video/x-raw, width=1280, height=720, framerate=30/1 ! videoconvert ! appsink'
out_pipeline = 'appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! video/x-raw, format=BGRx ! nvvidconv ! omxh264enc ! video/x-h264, stream-format=byte-stream ! h264parse ! rtph264pay pt=96 config-interval=1 ! udpsink host=192.168.178.63 port=5000'

#cam2 = vStream(camSet2, dispW, dispH, 0.5) # not working good, needs some configuration
cam2 = vStream(1, dispW, dispH, 0.5)

dispW = int(cam2.capture.get(cv2.CAP_PROP_FRAME_WIDTH)) # returns 1280
dispH = int(cam2.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))# returns 720
#print("dispW : ", dispW)
#print("dispH : ", dispH)

out = cv2.VideoWriter(out_pipeline, 0, 60, (dispW,dispH)) # fps = 60

startTime = time.time()
font = cv2.FONT_HERSHEY_SIMPLEX
dtavg = 0
fps = 0

while True:
    try:
        myFrame2 = cam2.getFrame()
        cv2.rectangle(myFrame2, (0,0), (80,35), (0,0,255), 2)
        cv2.putText(myFrame2, 'webCam', (5,20), font, 0.5, (0,255,255), 1)
        cv2.rectangle(myFrame2, (0,35), (80,70), (0,0,255), -1)
        cv2.putText(myFrame2, str(round(fps,1)), (5,60), font, 0.5, (0,255,255), 1)

        cv2.imshow('webCam', myFrame2)
        cv2.moveWindow('webCam', 0, 0)

        out.write(myFrame2) # update the ouput stream pipeline

        dt = time.time() - startTime
        startTime = time.time()
        dtavg = 0.9*dtavg + 0.1*dt # low pass filter
        fps = 1/dtavg

    except:
        print('frame not available')

    if cv2.waitKey(1) == ord('q'):
        cam2.capture.release()
        cv2.destroyAllWindows()
        exit(1)
        #break

