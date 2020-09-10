import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while 1:
    _,img=cap.read()
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower=np.array([169,100,100])
    upper=np.array([189,255,255])
    masks=cv2.inRange(hsv,lower,upper)
    red=cv2.bitwise_and(img,img,mask=masks)
    cv2.imshow("original",red)
    k=cv2.waitKey(30) & 0xff
    if k==27:
             break
cap.release()
cv2.destroyAllWindows()
