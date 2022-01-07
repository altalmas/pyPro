import cv2

dispW = 320*2
dispH = 240*2
flip = 0 # or 2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam = cv2.VideoCapture(camSet) # Rasperri Pi Camera
#cam = cv2.VideoCapture(1) # for webcam

#dispW = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)) # used with webcam
#dispH = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))# used with webcam

x = 0
y = 10
dx = 3
dy = 3
while True:
    ret, frame = cam.read()    # --- Read the Frame
                               # --- Magic is here
    frame = cv2.rectangle(frame,(340,100),(400,170),(255,0,0),4)
    frame = cv2.circle(frame, (320,240), 50, (0,0,255), -1) # solid
    frame = cv2.circle(frame, (100,100), 20, (70,100,255), 3)
    fnt = cv2.FONT_HERSHEY_DUPLEX
    frame = cv2.putText(frame, 'my Text', (300,300), fnt, 1, (255,0,150), 2)
    frame = cv2.line(frame, (10,10), (630,470), (0,0,0), 4)
    frame = cv2.arrowedLine(frame, (10,470),(630,10),(255,255,255), 3)
    
    x = x+dx
    y = y+dy
    if x <=0 or x+100 >= 640:
        dx = dx * (-1)
    if y <=0 or y+150 >= 480:
        dy = dy * (-1)
    frame = cv2.rectangle(frame, (x,y),(x+100,y+150),(255,0,0),-1)
    
    cv2.imshow('piCam', frame) # --- Show the Frame
    cv2.moveWindow('piCam', 0,0)
    if cv2.waitKey(1)==ord('q'): # wait to press 'q'
        break

cam.release()
cv2.destroyAllWindows()

