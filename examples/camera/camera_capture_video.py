from time import sleep

from pitop import Camera

# Record a 10s video to ~/Camera/

cam = Camera()

cam.start_video_capture()
sleep(10)
cam.stop_video_capture()
