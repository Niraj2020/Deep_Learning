import cv2

img1 = cv2.imread("Data\\thor.jpg",0) #convert image into grayscale
img1 = cv2.resize(img1,(560,700))
img1 = cv2.flip(img1,-1)#it accept 3 parameters 0,-1,1
cv2.imshow("converted image==",img1)
k = cv2.waitKey(0) & 0xFF
if k == ord("q"):
    cv2.destroyAllWindows()