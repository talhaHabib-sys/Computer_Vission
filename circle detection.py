import cv2
import numpy as n
v=cv2.imread('C:\\Users\\Talha Habib\\Desktop\\pictures\\b.png')
gray=cv2.cvtColor(v,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray,5)
cricles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,100,param1=60,param2=40,minRadius=0,maxRadius=0)
detected=n.uint16(n.around(cricles))
for (x,y,r) in detected[0, :]:
            cv2.circle(v,(x,y),r,(0,255,0),2)
            if cv2.waitKey(0)==27:
                    break

                
cv2.imshow('output',v)

