import cv2

dispW = 320*2 # the more the width and height, the faster the 
dispH = 240*2 # recording will be. but still good for training
flip = 0 # or 2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

#cam = cv2.VideoCapture(camSet) # capture from connected Camera
cam = cv2.VideoCapture('videos/myCam.avi') # capture (reading) from file

#cam = cv2.VideoCapture(1) # for webcam - 0 or 1

"""
    Comment the folling line out when reading from the file
"""
#outVid = cv2.VideoWriter('videos/myCam.avi', cv2.VideoWriter_fourcc(*'XVID'), 21, (dispW,dispH)) # 21 is the frameRate

while True:
    ret, frame = cam.read()    # --- Read the Frame
                               # --- Magic is here
    cv2.imshow('piCam', frame) # --- Show the Frame
    cv2.moveWindow('piCam', 0, 0)

    """
       comment the following line out when reading from file
       keep the following line when writing from connected cam to file
    """
    # outVid.write(frame) # write the frame 
    
    """
    when reading from file, wait for 50 msec
    when writing to file, wait only 1 msec
    """
    if cv2.waitKey(50)==ord('q'): # wait to press 'q'
        break

cam.release()
outVid.release()
cv2.destroyAllWindows()
