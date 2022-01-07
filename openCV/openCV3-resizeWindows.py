import cv2

dispW = 320*3
dispH = 240*3
flip = 0 # or 2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

# ----- Rasperri Pi CAM -----
cam = cv2.VideoCapture(camSet)

# ----- web CAM ------
#cam = cv2.VideoCapture(1) 
#cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    ret, frame = cam.read()    # --- Read the Frame
                               # --- Magic is here
    cv2.imshow('piCam', frame) # --- Show the Frame
    cv2.moveWindow('piCam', 700,0)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameSmall = cv2.resize(frame,(320,240))
    graySmall = cv2.resize(gray,(320,240))

    cv2.imshow('piSmall', frameSmall)
    cv2.imshow('BW',graySmall)
    cv2.imshow('piCam2',frameSmall)
    cv2.imshow('BW2', graySmall)

    cv2.moveWindow('piSmall', 0,0)
    cv2.moveWindow('BW', 0, 265)
    cv2.moveWindow('piCam2', 385, 0)
    cv2.moveWindow('BW2', 385, 265)

    if cv2.waitKey(1)==ord('q'): # wait to press 'q'
        break

cam.release()
cv2.destroyAllWindows()
