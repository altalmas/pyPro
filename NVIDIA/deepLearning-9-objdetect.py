import jetson.inference
import jetson.utils
import time
import numpy as np
import cv2

fpsFiltered = 0
timeStamp = time.time()

net = jetson.inference.detectNet('ssd-mobilenet-v2', threshold = 0.5) # when threshold is low : recognize alot of stuff
dispW = 1280
dispH = 720
flip = 0
font = cv2.FONT_HERSHEY_SIMPLEX
#font = jetson.utils.cudaFont()

#camSet='nvarguscamerasrc wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=2 brightness=2 saturation=-0.2 ! appsink'
#cam = cv2.VideoCapture(camSet)
cam = cv2.VideoCapture('/dev/video1')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)

#cam = jetson.utils.gstCamera(dispW,dispH, '0')
#cam = jetson.utils.gstCamera(displayW,displayH, '/dev/video1')
#disp = jetson.utils.glDisplay()

#while disp.IsOpen():
while True:
    _,img = cam.read()
    height = img.shape[0]
    width = img.shape[1]

    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA).astype(np.float32)
    frame = jetson.utils.cudaFromNumpy(frame)

    detections = net.Detect(frame, width, height) # detection is here
    for detect in detections:
        #print(detect)
        ID = detect.ClassID
        top = int(detect.Top)
        left = int(detect.Left)
        bottom = int(detect.Bottom)
        right = int(detect.Right)
        item = net.GetClassDesc(ID)
        #print(item, top, left, bottom, right)
        tk = 1
        if item == 'cat': # haha
            tk = -1
        cv2.rectangle(img, (left, top), (right,bottom), (0,255,0), tk)
        cv2.putText(img, item, (left, top+20), font, 0.75, (0,0,255), 2)

    dt = time.time()- timeStamp
    timeStamp = time.time()
    fps = 1/dt
    fpsFiltered = 0.9*fpsFiltered + 0.1*fps
    print(str(round(fpsFiltered,1)) + ' fps ')

    cv2.putText(img, str(round(fpsFiltered,1)) + ' fps', (0,30), font, 1,(0,0,255), 2)
    cv2.imshow('detCam', img)
    cv2.moveWindow('detCam', 0, 0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
