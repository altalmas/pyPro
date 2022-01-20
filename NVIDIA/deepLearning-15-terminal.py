import os

#piCam
camSet2 = 'gst-launch-1.0 nvarguscamerasrc ! "video/x-raw(memory:NVMM), format=NV12, width=1920, height=1080" ! nvv4l2h264enc insert-sps-pps=true ! h264parse ! rtph264pay pt=96 ! udpsink host=192.168.178.63 port=8001 sync=false -e'

#WebCam
camSet2 = 'gst-launch-1.0 v4l2src device="/dev/video1" ! video/x-raw, width=640, height=480, framerate=30/1 ! nvvidconv ! "video/x-raw(memory:NVMM), format=NV12" ! nvv4l2h264enc insert-sps-pps=true ! h264parse ! rtph264pay pt=96 ! udpsink host=192.168.178.63 port=8001 sync=false -e'

#run in terminal
os.system(camSet2)
