import cv2
import numpy as np

dispW = 320*2
dispH = 240*2
flip = 0 # or 2

img1 = np.zeros((dispH,dispW,1),np.uint8)
img1[:,0:320] = [255] # make the left half white
img2 = np.zeros((dispH,dispW,1), np.uint8)
img2[190:290,270:370] = [255]
bitAnd = cv2.bitwise_and(img1,img2)
bitOr = cv2.bitwise_or(img1,img2)
bitXor = cv2.bitwise_xor(img1,img2)

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam = cv2.VideoCapture(camSet) # Rasperri Pi Camera
#cam = cv2.VideoCapture(1) # for webcam

while True:
    ret, frame = cam.read()    # --- Read the Frame
                               # --- Magic is here

    frame = cv2.bitwise_and(frame,frame,mask = bitXor)

    cv2.imshow('piCam', frame) # --- Show the Frame
    cv2.imshow('img1',img1)
    cv2.imshow('img2',img2)
    cv2.imshow('and',bitAnd)
    cv2.imshow('or', bitOr)
    cv2.imshow('xor', bitXor)

    cv2.moveWindow('piCam', 0, 0)
    cv2.moveWindow('img1', 0, 500)
    cv2.moveWindow('img2', 700, 0)
    cv2.moveWindow('and', 700,500)
    cv2.moveWindow('or', 1340, 0)
    cv2.moveWindow('xor', 1340, 500)


    if cv2.waitKey(1)==ord('q'): # wait to press 'q'
        break

cam.release()
cv2.destroyAllWindows()
