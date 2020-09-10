import cv2

face_cascade=cv2.CascadeClassifier('C:\\Users\\Talha Habib\\Downloads\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier('C:\\Users\\Talha Habib\\Downloads\\opencv\\sources\\data\\haarcascades\\haarcascade_eye.xml')
face=cv2.CascadeClassifier('C:\\Users\\Talha Habib\\Downloads\\opencv\\sources\\data\\haarcascades\\haarcascade_smile.xml')

cap=cv2.VideoCapture(0)
while 1:
        ret,img=cap.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.1,5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            rog=gray[y:y+h,x:x+h]
            roc=img[y:y+h,x:x+h]
            roig=gray[y:y+h,x:x+h]
            rocg=img[y:y+h,x:x+h]
            e=eye.detectMultiScale(rog)
            f=face.detectMultiScale(rocg,1.4,5)
            for (ex,ey,ew,eh) in e:
                cv2.rectangle(roc,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
            for(exx,eyy,eww,ehh) in f:
                    cv2.rectangle(rocg,(exx,eyy),(exx+eww,eyy+ehh),(0,255,0),2)
            
        
        cv2.imshow('img',img) 
        k=cv2.waitKey(30) & 0xff
        if k==27:
             break
cap.release()
cv2.destroyAllWindows()

     
