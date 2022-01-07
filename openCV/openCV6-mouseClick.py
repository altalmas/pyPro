# Lesson 17 in youtube
import cv2
import numpy as np
evt = -1
coord = []
img = np.zeros((250,250,3), np.uint8)

def click(event,x,y,flags,params):
    global pnt
    global evt
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Mouse event was : ', event)
        print(x,' , ',y)
        pnt = (x,y)
        coord.append(pnt)
        print(coord)
        evt = event
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x,y)
        # Value   = pixel = frame (row,column,colorIndex)
        blueValue = frame[y,x,0] # B
        greenValue = frame[y,x,1] # G
        redValue = frame[y,x,2] # R
        print(blueValue, greenValue, redValue)
        colorString = str(blueValue)+','+str(greenValue)+','+str(redValue)
        img[:]=[blueValue,greenValue,redValue]
        fnt = cv2.FONT_HERSHEY_PLAIN
        r = 255-int(redValue)
        g = 255-int(greenValue)
        b = 255-int(blueValue)
        tp = (b,g,r)
        cv2.putText(img,colorString,(10,25),fnt,1,tp,2)
        cv2.imshow('myColor',img)

dispW = 320*2
dispH = 240*2
flip = 0 # or 2

cv2.namedWindow('piCam') # define the window
cv2.setMouseCallback('piCam', click) # mouse listener

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam = cv2.VideoCapture(camSet) # Rasperri Pi Camera
#cam = cv2.VideoCapture(1) # for webcam

while True:
    ret, frame = cam.read()    # --- Read the Frame
                               # --- Magic is here
 #   if evt == 1:
 #       cv2.circle(frame,pnt,5,(0,0,255),-1)
 #       fnt = cv2.FONT_HERSHEY_PLAIN
 #       myStr = str(pnt)
 #       cv2.putText(frame, myStr, pnt, fnt, 1, (255,0,0), 2)
        
    for points in coord:
        cv2.circle(frame,points,5,(0,0,255),-1)
        fnt = cv2.FONT_HERSHEY_PLAIN
        myStr = str(points)
        cv2.putText(frame, myStr, points, fnt, 1, (255,0,0), 2)

    cv2.imshow('piCam', frame) # --- Show the Frame
    cv2.moveWindow('piCam', 0,0)

    key = cv2.waitKey(1)
    if key==ord('q'): # wait to press 'q'
        break
    if key==ord('c'):
        coord = []

cam.release()
cv2.destroyAllWindows()
