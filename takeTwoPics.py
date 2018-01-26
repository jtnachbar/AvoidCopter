import cv2
import sys
import time
from datetime import datetime

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

# Get enumerations with the expression cv2.cv.YOUR_ENUM
cam1.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 160)
cam1.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 120)
cam2.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 160)
cam2.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 120)

numCycles = int(sys.argv[1] if len(sys.argv) > 1 else 100)
pauseTime = int(sys.argv[2] if len(sys.argv) > 2 else 5)

for i in range(1, numCycles):
  _, img1 = cam1.read()
  _, img2 = cam2.read()
  timestamp = str(datetime.now())
  path = '/home/odroid/images/' + timestamp
  cv2.imwrite(path+'-1.png', img1)
  cv2.imwrite(path+'-2.png', img2)
  print("Saved file pair %d at %s" % (i, timestamp))
  time.sleep(pauseTime)

# If we don't release the cameras, bad things could happen
cam1.release()
cam2.release()
del(cam1)
del(cam2)
