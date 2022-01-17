# Lesson 52 : made some modifications for the picture of the Pi Camera

from time import time
import cv2
import numpy as np

print(cv2.__version__)
dispW=640
dispH=480
flip=0
#Uncomment These next Two Line for Pi Camera
""" The following 'camSet' variable can be changed according to the settings that we get when we write in the terminal : 
    $ gst-inspect-1.0 nvarguscamerasrc
    for example, here we are adding 'wbmode=3'
    also, we added 'wbmode=3'
"""
camSet1='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
camSet2='nvarguscamerasrc wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=2 brightness=2 saturation=-0.2 ! appsink'

cam1= cv2.VideoCapture(camSet2)

#Or, if you have hstacka WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)
while True:
    ret, frame1 = cam1.read()
    cv2.imshow('nanoCam',frame1)
    cv2.moveWindow('nanoCam', 0, 0)
    if cv2.waitKey(1)==ord('q'):
        break
cam1.release()
cv2.destroyAllWindows()
