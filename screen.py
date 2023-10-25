import cv2

vidcap=cv2.VideoCapture(0)
ret,image=vidcap.read()

count=0

while True:
    if ret==True:
        cv2.imwrite("frame\\imgN%d.jpg" % count, image)
        vidcap.set(cv2.CAP_PROP_POS_MESC, (count**100))
        ret, image=vidcap.read()
        cv2.imshow("res", image)
        print("Read a new frame:", count, ret)
        count+=1
        if cv2.waitKey() & 0xFF==ord("q"):
            break
            cv2.destroyAllWindows()
    else:
        break
 
vidcap.release()
cv2.destroyAllWindows()            