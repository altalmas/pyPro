# In this program, we are using the Jetson (NVIDIA) libraries that are fast enough for their product (Jetson Nano), 
# however, NVIDIA libraries are not the best in controlling the image, 
# theirfore, we here use cv2 libraries again to control the image without paying a lot of fps (frames per second)

#from sys import builtin_module_names
import jetson.inference
import jetson.utils
import cv2
import numpy as np
import time

width = 1280
height = 720

#dispW = width
#dispH = height
#flip = 2
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

# --- Using Camera from cv2 Lib ---
#cam = cv2.VideoCapture(camSet) # Rasperri Pi Camera from cv2
#cam = cv2.VideoCapture(1) # for webcam from cv2
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

# --- Using Camera from Jetson Lib ---
cam = jetson.utils.gstCamera(width, height, '/dev/video1') # WebCam from jetson lib
#cam = jetson.utils.gstCamera(width, height, '0') # PiCam from jetson lib
#display = jetson.utils.glDisplay()

# --- Models --- : These models are different in their capabilities of recognizing stuff
net = jetson.inference.imageNet('googlenet')
#net = jetson.inference.imageNet('alexnet')
#net = jetson.inference.imageNet('resnet-50')
#net = jetson.inference.imageNet('resnet-101')
# --------------

timeMark = time.time()
fpsFilter = 0

#font = jetson.utils.cudaFont()
font = cv2.FONT_HERSHEY_SIMPLEX

#while display.IsOpen():
while True:
    #_, frame = cam.read() # getting frame from cv2 Lib
    #img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA).astype(np.float32)
    #img = jetson.utils.cudaFromNumpy(img)
    #classID, confidence = net.Classify(img, width, height)

    frame, width, height = cam.CaptureRGBA(zeroCopy = 1) # getting frame from Jetson Lib
    #frame, width, height = cam.CaptureRGBA() # getting frame from Jetson Lib
    classID, confidence = net.Classify(frame, width, height)
    item = net.GetClassDesc(classID)
    #font.OverlayText(frame, width, height, str(round(fpsFilter, 1)) + ' fps : ' + item, 5, 5 , font.Magenta, font.Blue)
    #display.RenderOnce(frame, width, height)

    dt = time.time() - timeMark
    fps = 1/dt
    fpsFilter = 0.9 * fpsFilter + 0.1*fps
    timeMark = time.time()

    frame = jetson.utils.cudaToNumpy(frame, width, height, 4) # 4 is the dimension of the array (RBGA)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR).astype(np.uint8)
    cv2.putText(frame, str(round(fpsFilter,1))+' fps : '+ item, (0,30), font, 1, (0,0,255), 2)
    cv2.imshow('recCam', frame)
    cv2.moveWindow('recCam', 0, 0)

    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

