# lesson 26
import cv2
import numpy as np

dispW = 320*2
dispH = 240*2
flip = 0 # or 2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam = cv2.VideoCapture(camSet) # Rasperri Pi Camera
#cam = cv2.VideoCapture(1) # for webcam

blank = np.zeros([dispH,dispW,1], np.uint8)

while True:
    ret, frame = cam.read()    # --- Read the Frame
                               # --- Magic is here
                               
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(frame[50,45,0])

    #print(gray.shape)
    #print(gray.size)
    #b = cv2.split(frame)[0]
    #g = cv2.split(frame)[1]
    #r = cv2.split(frame)[2]
    b, g, r = cv2.split(frame)
 #   cv2.imshow('b', b)
 #   cv2.moveWindow('b', 700, 0)
 #   cv2.imshow('g', g)
 #   cv2.moveWindow('g', 0, 500)
 #   cv2.imshow('r', r)
 #   cv2.moveWindow('r', 700, 500)

 #   b[:] = b[:] * 1.2
    merge = cv2.merge((b,g,r))

    bb = cv2.merge((b,blank,blank))
    gg = cv2.merge((blank,g,blank))
    rr = cv2.merge((blank,blank,r))

    cv2.imshow('bb', bb)
    cv2.moveWindow('bb', 700, 0)
    cv2.imshow('gg', gg)
    cv2.moveWindow('gg', 0, 500)
    cv2.imshow('rr', rr)
    cv2.moveWindow('rr', 700, 500)

    # blank[0:240,0:320] = 125

    cv2.imshow('piCam', frame) # --- Show the Frame
    cv2.imshow('blank', blank)
    cv2.imshow('merge', merge)

    cv2.moveWindow('piCam', 0, 0)
    cv2.moveWindow('blank', 1200, 0)
    cv2.moveWindow('merge', 1200, 500)

    if cv2.waitKey(1)==ord('q'): # wait to press 'q'
        break

cam.release()
cv2.destroyAllWindows()
