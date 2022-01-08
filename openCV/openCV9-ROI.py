import cv2

dispW = 320*2
dispH = 240*2
flip = 0 # or 2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam = cv2.VideoCapture(camSet) # Rasperri Pi Camera
#cam = cv2.VideoCapture(1) # for webcam

while True:
    ret, frame = cam.read()    # --- Read the Frame
                               # --- Magic is here
    roi = frame[50:250,200:400].copy()
    roiGray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    roiGray = cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR) # bring it back to form

    frame[50:250,200:400] = roiGray

    cv2.imshow('ROIGray',roiGray)
    cv2.imshow('ROI',roi)
    cv2.imshow('piCam', frame) # --- Show the Frame
    
    cv2.moveWindow('piCam', 0, 0)
    cv2.moveWindow('ROI', 705,0)
    cv2.moveWindow('ROIGray', 705, 200)

    if cv2.waitKey(1)==ord('q'): # wait to press 'q'
        break

cam.release()
cv2.destroyAllWindows()
