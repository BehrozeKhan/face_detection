import numpy as np
import cv2

print("Face Detection in Opencv Pyhton.")
img = cv2.imread('3.jpg' , 1)
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
path = "haarcascade_frontalface_default.xml"
face = cv2.CascadeClassifier(path)
detect = face.detectMultiScale(gray, scaleFactor=1.10,
	minNeighbors = 5, minSize = (40,40))

for(x,y,w,h) in detect:
	cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
cv2.imshow("Face_detection" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
