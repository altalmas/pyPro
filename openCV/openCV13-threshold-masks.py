# Lesson 24 on Youtube

import cv2
print(cv2.__version__)

def nothing():
    pass
cv2.namedWindow('blended')
cv2.createTrackbar('BlendValue', 'blended', 50, 100, nothing)

dispW = 320*1
dispH = 240*1
flip = 0 # or 2

cvLogo = cv2.imread('cv.jpg')
cvLogo = cv2.resize(cvLogo, (dispW,dispH))

cvLogoGray = cv2.cvtColor(cvLogo, cv2.COLOR_BGR2GRAY)
cv2.imshow('cvLOGOGray', cvLogoGray)
cv2.moveWindow('cvLogoGray', 385,100)

_,BGMask = cv2.threshold(cvLogoGray,225,255,cv2.THRESH_BINARY)
cv2.imshow('BGMask', BGMask)
cv2.moveWindow('BGMask', 0,710)

FGMask = cv2.bitwise_not(BGMask) # invert it
cv2.imshow('FGMask',FGMask)
cv2.moveWindow('FGMask', 385, 710)

maskedLogo = cv2.bitwise_and(cvLogo,cvLogo, mask=FGMask)
cv2.imshow('maskedLogo', maskedLogo)
cv2.moveWindow('maskedLogo', 700, 100)

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam = cv2.VideoCapture(camSet) # Rasperri Pi Camera
#cam = cv2.VideoCapture(1) # for webcam

while True:
    ret, frame = cam.read()    # --- Read the Frame
                               # --- Magic is here
    BG = cv2.bitwise_and(frame,frame,mask = BGMask)
    FG = cv2.bitwise_and(frame,frame,mask = FGMask)
    compImage = cv2.add(maskedLogo, BG)

    BV = cv2.getTrackbarPos('BlendValue', 'blended')/100
    BV2 = 1 - BV
    blended = cv2.addWeighted(frame, BV, maskedLogo, BV2, 0)

    compImage2 = cv2.add(BG,blended)


    cv2.imshow('piCam', frame) # --- Show the Frame
    cv2.imshow('BG', BG)
    cv2.imshow('FG', FG)
    cv2.imshow('compImage', compImage)
    cv2.imshow('blended', blended)
    cv2.imshow('compImage2', compImage2)

    cv2.moveWindow('piCam', 0, 100)
    cv2.moveWindow('BG', 0,380)
    cv2.moveWindow('FG', 385, 380)
    cv2.moveWindow('compImage', 700, 380)
    cv2.moveWindow('blended', 1000, 100)
    cv2.moveWindow('compImage2', 1000, 380)

    if cv2.waitKey(1)==ord('q'): # wait to press 'q'
        break

cam.release()
cv2.destroyAllWindows()
