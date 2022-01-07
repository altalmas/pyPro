import cv2

dispW = 320*4
dispH = 240*4
flip = 2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

piCam = cv2.VideoCapture(camSet) # Rasperri Pi Camera
webCam = cv2.VideoCapture(1) # for webcam

while True:
    ret, frame = piCam.read()
    ret, frame2 = webCam.read()
    cv2.imshow('piCam', frame)
    cv2.imshow('webCam', frame2)

    if cv2.waitKey(1)==ord('q'): # wait to press 'q'
        break

cam.release()
cv2.destroyAllWindows()
