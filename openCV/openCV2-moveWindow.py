import cv2

dispW = 320*1
dispH = 240*1
flip = 0 # or 2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam = cv2.VideoCapture(camSet) # Rasperri Pi Camera
#cam2 = cv2.VideoCapture(1) # for webcam

while True:
    ret, frame = cam.read()    # --- Read the Frame
    #ret, frame2 = cam2.read()
                               # --- Magic is here

    cv2.imshow('piCam', frame) # --- Show the Frame
    cv2.moveWindow('piCam',0, 0)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayPiVideo',gray)
    cv2.moveWindow('grayPiVideo', 0, 320)

    cv2.imshow('piCam2', frame)
    cv2.moveWindow('piCam2',400, 0)

    gray2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayPiVideo2',gray2)
    cv2.moveWindow('grayPiVideo2', 400, 320)

    if cv2.waitKey(1)==ord('q'): # wait to press 'q'
        break

cam.release()
cv2.destroyAllWindows()
