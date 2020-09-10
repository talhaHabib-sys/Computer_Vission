import cv2
import numpy as n
image=cv2.imread('C:\\Users\\Talha Habib\\Desktop\\pictures\\sh.png')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_,thrash=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)
con,_=cv2.findContours(thrash,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for c in con:
    approx=cv2.approxPolyDP(c,0.01*cv2.arcLength(c,True),True)
    cv2.drawContours(image,[approx],0,(0,255,0),4)
    x=approx.ravel()[0]-5
    y=approx.ravel()[1]+7
    if len(approx)==3:
        cv2.putText(image,"Triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    elif len(approx)==4:
        x1,y1,w,h=cv2.boundingRect(approx)
        ratio=float(w)/h
        print(ratio)
        if ratio >= 0.95 and ratio <=1.95:    
                cv2.putText(image,"Square",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
        elif ratio >=0.45 and ratio <=1.25:
            cv2.putText(image,"quadrilateral",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
        else:
            cv2.putText(image,"rectangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
            
    elif len(approx)==5:
        cv2.putText(image,"Pantagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    elif len(approx)==10:
        cv2.putText(image,"Star",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    else:
        cv2.putText(image,"Circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))

cv2.imshow("output",image)
