import cv2

dispW = 320*2
dispH = 240*2
flip = 0 # or 2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

#cam = cv2.VideoCapture(camSet) # Rasperri Pi Camera
cam = cv2.VideoCapture(1) # for webcam

face_cascade = cv2.CascadeClassifier('cascade/face.xml')
eye_cascade = cv2.CascadeClassifier('cascade/eye.xml')
smile_cascade = cv2.CascadeClassifier('cascade/smile.xml')

while True:
    ret, frame = cam.read()    # --- Read the Frame
                               # --- Magic is here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # 1.3 and 5 are tuning params
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 3)
    #smiles = smile_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
    for (x,y,w,h) in eyes:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
 #   for (x,y,w,h) in smiles:
 #       cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)

    cv2.imshow('piCam', frame) # --- Show the Frame
    cv2.moveWindow('piCam', 0, 0)
    if cv2.waitKey(1)==ord('q'): # wait to press 'q'
        break

cam.release()
cv2.destroyAllWindows()
