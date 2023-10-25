import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
print("check===", cap.isOpened())

fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter("output.avi", fourcc, 20,0,(640, 480),0)

while(cap.isOpened()):
    ret, frame=cap.read()
    
    if ret==True:
        
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame=cv2.flip(frame,0)
        output.write(gray)
        
        cv2.imshow("Gray Frame", gray)
        cv2.imshow('Colorframe', frame)
        if cv2.waitKey(0) & 0xFF ==ord('q'):
            break
        else:
            break
        
        
    cap.release()
    output.release()
    cv2.destroyAllWindows()   