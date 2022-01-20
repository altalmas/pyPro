import cv2
import os

dispW = 320*2
dispH = 240*2
flip = 0 # or 2

# Rasperri Pi Camera
camSet='nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# for webcam
camSet='v4l2src device=/dev/video1 ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', framerate=30/1 ! videoconvert ! appsink'

cam = cv2.VideoCapture(camSet, cv2.CAP_GSTREAMER) # Either WebCam or PiCam
#cam = cv2.VideoCapture(1) # for webcam

while True:
    try:
        ret, frame = cam.read()     # --- Read the Frame
                                    # --- Magic is here
        frame = cv2.rectangle(frame,(340,100),(400,170),(255,0,0),4)
        print(frame.shape)
        cv2.imshow('piCam', frame) # --- Show the Frame
        cv2.moveWindow('piCam', 0, 0)
    except:
        print("No Camera")

    
    if cv2.waitKey(1)==ord('q'): # wait to press 'q'
        break

cam.release()
cv2.destroyAllWindows()
