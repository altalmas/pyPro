import cv2

dispW = 320*2
dispH = 240*2
flip = 0 # or 2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

#cam = cv2.VideoCapture(camSet) # Rasperri Pi Camera
cam = cv2.VideoCapture(1) # for webcam

while True:
    try:
        ret, frame = cam.read()    # --- Read the Frame
                               # --- Magic is here
        cv2.imshow('piCam', frame) # --- Show the Frame
    except:
        print("No Camera")
    if cv2.waitKey(1)==ord('q'): # wait to press 'q'
        break

cam.release()
cv2.destroyAllWindows()
