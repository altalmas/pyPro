import cv2

rCoord = []

def click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_LBUTTONUP:
        pos = (x,y)
        rCoord.append(pos)
    
dispW = 320*2
dispH = 240*2
flip = 0 # or 2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam = cv2.VideoCapture(camSet) # Rasperri Pi Camera
#cam = cv2.VideoCapture(1) # for webcam

cv2.namedWindow('piCam') # define the window
cv2.setMouseCallback('piCam', click) # mouse listener

while True:
    ret, frame = cam.read()    # --- Read the Frame
                               # --- Magic is here
    if  len(rCoord) != 0 and len(rCoord)%2 == 0:
        pnt1 = rCoord[len(rCoord)-2]
        pnt2 = rCoord[len(rCoord)-1]
        cv2.rectangle(frame, pnt1, pnt2, (0,255,0),3)
        if pnt2[1]>pnt1[1] and pnt2[0]>pnt1[0] :
            roi = frame[pnt1[1]:pnt2[1],pnt1[0]:pnt2[0]].copy()
            cv2.imshow('ROI', roi)
            cv2.moveWindow('ROI', 710, 0)

    if len(rCoord) > 0:
        print('length : ' + str(len(rCoord)))
        print(rCoord[len(rCoord)-1])

    cv2.imshow('piCam', frame) # --- Show the Frame
    cv2.moveWindow('piCam', 0, 0)        

    if cv2.waitKey(1)==ord('q'): # wait to press 'q'
        break

cam.release()
cv2.destroyAllWindows()
