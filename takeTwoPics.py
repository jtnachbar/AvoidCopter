import cv2

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

# Get enumerations witht he expression cv2.cv.YOUR_ENUM
#cam1.set(CV_CAP_PROP_FOURCC, CV_FOURCC('M', 'J', 'P', 'G'))
#cam2.set(CV_CAP_PROP_FOURCC, CV_FOURCC('M', 'J', 'P', 'G'))
cam1.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 160)
cam1.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 120)
cam2.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 160)
cam2.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 120)
#cam1.set(cv2.cv.CV_CAP_PROP_BRIGHTNESS, 5)
#cam2.set(cv2.cv.CV_CAP_PROP_BRIGHTNESS, 5)

def takePic(camera, file):
   _, img = camera.read()
   return cv2.imwrite(file, img)

#path = '/home/odroid/ImageTesting/'
print(takePic(cam1, 'test1.png'))
print(takePic(cam2, 'test2.png'))

cam1.release()
cam2.release()
del(cam1)
del(cam2)
