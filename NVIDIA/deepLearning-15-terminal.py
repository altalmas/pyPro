import os

camSet2 = 'gst-launch-1.0 nvarguscamerasrc ! "video/x-raw(memory:NVMM), format=NV12, width=1920, height=1080" ! nvv4l2h264enc insert-sps-pps=true ! h264parse ! rtph264pay pt=96 ! udpsink host=192.168.178.63 port=8001 sync=false -e'

os.system(camSet2)

