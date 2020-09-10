import cv2
import numpy as np
cap=cv2.VideoCapture(0)
_,frame=cap.read()
_,frame1=cap.read()
_,frame2=cap.read()
while 1:
        
        d=cv2.absdiff(frame1, frame2)
        grey=cv2.cvtColor(d,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(grey,(5,5),0)
        ret,th=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
        dilated=cv2.dilate(th,np.ones((3,3),np.uint8),iterations=3)
        eroded=cv2.erode(dilated,np.ones((3,3),np.uint8),iterations=3)
        c=cv2.findContours(eroded,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(frame1,c,-1,(0,0,255),2)
        cv2.imshow("output",frame1)
        if cv2.waitKey(0)==27:
            break
        frame1=frame2
        _,frame2=cap.read()
cv2.destroyAllWindows()
cap.release()

