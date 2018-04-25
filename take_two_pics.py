import cv2
import sys
from time import sleep
from datetime import datetime

# The folder to save the images
# Each image is labeled by timestamp
images_path = '/home/odroid/images/'

# Create objects for each camera
cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

# Reduce the resolution of the images for two reasons:
# - USB 2.0 cannot handle the full size
# - we didn't expect to need full quality for training
cam1.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 160)
cam1.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 120)
cam2.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 160)
cam2.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 120)

# These can be passed 
num_cycles = int(sys.argv[1] if sys.argv[1] else 100)
pause_time = int(sys.argv[2] if sys.argv[2] else 5)

for i in range(1, num_cycles + 1):
  _, img1 = cam1.read()
  _, img2 = cam2.read()
  timestamp = str(datetime.now().time())
  cv2.imwrite(images_path + timestamp + '-1.png', img1)
  cv2.imwrite(images_path + timestamp + '-2.png', img2)
  print("Saved file pair %d at %s" % (i, timestamp))
  sleep(pause_time)

# If we don't release the cameras, bad things could happen
cam1.release()
cam2.release()
del(cam1)
del(cam2)
