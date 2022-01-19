import cv2

dispW = 320*2
dispH = 240*2
flip = 0 # or 2

# Rasperri Pi Camera
camSet='nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

# for webcam
#camSet='v4l2src device=/dev/video1 ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', framerate=30/1 ! videoconvert ! appsink'

#camSet = "udpsrc address=0.0.0.0 port=8001 caps='application/x-rtp, encoding-name=(string)H264, payload=(int)96' ! rtph264depay ! queue ! h264parse ! nvv4l2decoder ! nv3dsink -e"

cam = cv2.VideoCapture(camSet) # Either WebCam or PiCam
#cam = cv2.VideoCapture(1) # for webcam

while True:
#try:
    ret, frame = cam.read()    # --- Read the Frame
                            # --- Magic is here
    cv2.imshow('piCam', frame) # --- Show the Frame
#except:
    #print("No Camera")
    if cv2.waitKey(1)==ord('q'): # wait to press 'q'
        break

cam.release()
cv2.destroyAllWindows()
