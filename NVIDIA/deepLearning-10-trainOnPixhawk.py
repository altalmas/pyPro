""""
Need to watch lesson 55 : it is also important to train on more than 1 object, here for 
example it sees pixhawk only, and always displays pixhawk
We need to :
    1. create swap spacing by using the SD card as a memory
        $ sudo fallocate -l 4G /mnt/4GB.swap
        $ sudo sudo mkswap /mnt/4GB.swap
        $ sudo swapon /mnt/4GB.swap
    2. edit the /etc/fstab file
        $ sudo gedit /etc/fstab
    3. add to the end the following line:
        /mnt/4GB.swap none swap sw 0 0
    4. save the file and close

Then, we will need to 
    1. create a folder in which we will put our training data:
        $ cd ~/Downloads/jetson-inference
        $ mkdir myTrain
        $ cd myTrain
    2. create a text file :
        $ gedit labels.txt
    3. give the names of the classes by putting them on top or each other
        Arduino Nano
        Arduino Uno
        Pixhawk
        Raspberry Pi Zero
    4. save and close

Then, we will start capturing the training data
    1.  
        $ cd ~/Downloads/jetson-inference/tools
        $ camera-capture --width=800 --height=600 --camera=/dev/video1
    2. then, we will need to set the:
    Path to the data set: ~/Downloads/jetson-inference/myTrain
    Path to labels.txt : ~/Downloads/jetson-inference/myTrain/labels.txt
    and choose whether now we will take a pictures for 'train or val or test'

    3. make at least 100 pictures for 'train'
       make at least 20 pictures for 'val'
       make at least 5 pics for 'test'

    4. now, after finishing, you will see that the directory ~/Downloads/jetson-inference/myTrain
       having new directories

Then, 
    1. Now, we need to use NVIDIA ready-code to make the traning and obtain a new model from 
       their .py file. the new model that I will make will be called 'myModelName'.

        $ cd ~/Downloads/jetson-inference/python/training/classification
        $ python3 train.py --model-dir=myModelName ~/Downloads/jetson-inference/myTrain

        It will keep running for some good time, (700 pictures ~ 45 mins)

    2. while staying in ~/Downloads/jetson-inference/python/training/classification

        $ python3 onnx_export.py --model-dir=myModelName

        It will run for 2-10 mins


Now, use the following program :)

"""
import jetson.inference
import jetson.utils
import cv2
import numpy as np
import time
width=800
height=600
dispW=width
dispH=height
flip=2
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance  contrast=1.5 brightness=-.3 saturation=1.2 ! appsink  '
#cam1=cv2.VideoCapture(camSet)
cam1=cv2.VideoCapture('/dev/video1')
cam1.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam1.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
net=jetson.inference.imageNet('googlenet',['--model=/home/abdallah/Downloads/jetson-inference/python/training/classification/myModel/resnet18.onnx','--input_blob=input_0','--output_blob=output_0','--labels=/home/abdallah/Downloads/jetson-inference/myTrain/labels.txt'])
font=cv2.FONT_HERSHEY_SIMPLEX
timeMark=time.time()
fpsFilter=0
while True:
    _,frame=cam1.read()
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA).astype(np.float32)
    img=jetson.utils.cudaFromNumpy(img)
    classID, confidence =net.Classify(img, width, height)
    item=''
    item =net.GetClassDesc(classID)
    dt=time.time()-timeMark
    fps=1/dt
    fpsFilter=.95*fpsFilter +.05*fps
    timeMark=time.time()
    cv2.putText(frame,str(round(fpsFilter,1))+' fps '+item,(0,30),font,1,(0,0,255),2)
    cv2.imshow('recCam',frame)
    cv2.moveWindow('recCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam1.releast()
cv2.destroyAllWindows()

