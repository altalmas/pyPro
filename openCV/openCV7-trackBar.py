import cv2

dispW = 320*2
dispH = 240*2
flip = 0 # or 2

def nothing():
    pass # does nothing

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam = cv2.VideoCapture(camSet) # Rasperri Pi Camera
#cam = cv2.VideoCapture(1) # for webcam

cv2.namedWindow('piCam')
cv2.createTrackbar('xVal','piCam',25, dispW, nothing)
cv2.createTrackbar('yVal','piCam',25, dispH, nothing)
cv2.createTrackbar('recWidth','piCam',25, dispW, nothing)
cv2.createTrackbar('recHeight','piCam',25, dispH, nothing)

while True:
    ret, frame = cam.read()    # --- Read the Frame
                               # --- Magic is here
    xVal = cv2.getTrackbarPos('xVal','piCam')
    yVal = cv2.getTrackbarPos('yVal','piCam')
    recWidth = cv2.getTrackbarPos('recWidth','piCam')
    recHeight = cv2.getTrackbarPos('recHeight','piCam')
    cv2.circle(frame,(xVal,yVal),5,(255,0,0),-1)
    cv2.rectangle(frame, (xVal,yVal), (xVal+recWidth,yVal+recHeight), (0,255,0), 2)

    cv2.imshow('piCam', frame) # --- Show the Frame
    cv2.moveWindow('piCam', 0,0)
    if cv2.waitKey(1)==ord('q'): # wait to press 'q'
        break
    
cam.release()
cv2.destroyAllWindows()
