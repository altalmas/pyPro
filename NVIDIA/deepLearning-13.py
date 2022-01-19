# dont mind this code

import jetson.inference
import jetson.utils
import time

fpsFiltered = 0
timeStamp = time.time()

net = jetson.inference.detectNet('ssd-mobilenet-v2', threshold = 0.5) # when threshold is low : recognize alot of stuff
displayW = 1280
displayH = 720
cam = jetson.utils.gstCamera(displayW,displayH, '/dev/video1')
disp = jetson.utils.videoOutput()

font = jetson.utils.cudaFont()

while disp.IsStreaming():
    frame, width, height = cam.CaptureRGBA()
    detections = net.Detect(frame, width, height) # detection is here
    disp.Render(frame)
    #dt = time.time()- timeStamp
    #timeStamp = time.time()
    #fps = 1/dt
    #fpsFiltered = 0.9*fpsFiltered + 0.1*fps
    #print(str(round(fpsFiltered,1)) + ' fps ')
