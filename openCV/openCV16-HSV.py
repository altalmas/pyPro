# Lesson 27 on Youtube

# Hue : 0 - 179
# Saturation : 0 - 255
# Value : 0 - 255

import cv2
import numpy as np

def nothing():
    pass

cv2.namedWindow('Trackbars')

cv2.createTrackbar('hueLow', 'Trackbars', 50, 179, nothing)
cv2.createTrackbar('hueHigh', 'Trackbars', 100, 179, nothing)
cv2.createTrackbar('hueLow2', 'Trackbars', 50, 179, nothing)
cv2.createTrackbar('hueHigh2', 'Trackbars', 100, 179, nothing)
cv2.createTrackbar('satLow', 'Trackbars', 50, 255, nothing)
cv2.createTrackbar('satHigh', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('valLow', 'Trackbars', 100, 255, nothing)
cv2.createTrackbar('valHigh', 'Trackbars', 255, 255, nothing)

cv2.moveWindow('Trackbars', 1320, 0)

dispW = 320*2
dispH = 240*2
flip = 0 # or 2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

#cam = cv2.VideoCapture(camSet) # Rasperri Pi Camera
cam = cv2.VideoCapture(1) # for webcam

while True:
    ret, frame = cam.read()    # --- Read the Frame
    #frame = cv2.imread('smarties.png')
                               # --- Magic is here

    frame = cv2.resize(frame,(320,240))
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hueLow = cv2.getTrackbarPos('hueLow', 'Trackbars')
    hueHigh = cv2.getTrackbarPos('hueHigh', 'Trackbars')
    hueLow2 = cv2.getTrackbarPos('hueLow2', 'Trackbars')
    hueHigh2 = cv2.getTrackbarPos('hueHigh2', 'Trackbars')

    satLow = cv2.getTrackbarPos('satLow', 'Trackbars')
    satHigh = cv2.getTrackbarPos('satHigh', 'Trackbars')

    valLow = cv2.getTrackbarPos('valLow', 'Trackbars')
    valHigh = cv2.getTrackbarPos('valHigh', 'Trackbars')

    l_b = np.array([hueLow,satLow,valLow]) # lower bound
    u_b = np.array([hueHigh,satHigh,valHigh]) # higher bound
    l_b2 = np.array([hueLow2,satLow,valLow]) # lower bound
    u_b2 = np.array([hueHigh2,satHigh,valHigh]) # higher bound

    FGMask = cv2.inRange(hsv,l_b,u_b)
    FGMask2 = cv2.inRange(hsv,l_b2, u_b2)
    FGMaskComp = cv2.add(FGMask,FGMask2)
    cv2.imshow('FGMask', FGMaskComp)
    cv2.moveWindow('FGMask', 0,410)

    FG = cv2.bitwise_and(frame, frame, mask=FGMaskComp)
    cv2.imshow('FG', FG)
    cv2.moveWindow('FG', 500, 0)

    BGMask = cv2.bitwise_not(FGMaskComp)
    cv2.imshow('BGMask', BGMask)
    cv2.moveWindow('BGMask', 500, 410)

    BG = cv2.cvtColor(BGMask, cv2.COLOR_GRAY2BGR) # making the matrix the write size
    #cv2.imshow('BG', BG)
    #cv2.moveWindow('BG', 500, 0)

    final = cv2.add(FG,BG)
    cv2.imshow('final', final)
    cv2.moveWindow('final', 900, 0)
      
    cv2.imshow('piCam', frame) # --- Show the Frame
    cv2.moveWindow('piCam', 0, 0)



    if cv2.waitKey(1)==ord('q'): # wait to press 'q'
        break

cam.release()
cv2.destroyAllWindows()
