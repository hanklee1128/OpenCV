import cv2

img=cv2.imread("lenna.jpg")

#用gray image即可辨識
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faceCascade=cv2.CascadeClassifier("face_detect.xml")
#參數: 圖片,縮小倍數,框到臉
faceCascade.detectMultiScale(gray,1.1,3)
