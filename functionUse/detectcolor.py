from re import A
import cv2
import numpy as np
from sqlalchemy import true

img=cv2.imread("bear.jpg")#讀入圖片

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#BRG轉成HSV
#HSV一種表示顏色的方法
#用HSV比RGB更容易過濾顏色
#Hue色調 Saturation飽和度 Value亮度


#動態控制條找顏色
cv2.namedWindow("Track bar")#創建一視窗 called track bar
cv2.resizeWindow("Track bar",640,320)#resize 寬640,高320

cv2.createTrackbar("Hue min","Track bar",0,179,np.empty)
cv2.createTrackbar("Hue max","Track bar",179,179,np.empty)
cv2.createTrackbar("Sat min","Track bar",0,179,np.empty)
cv2.createTrackbar("Sat max","Track bar",255,255,np.empty)
cv2.createTrackbar("Val min","Track bar",0,179,np.empty)
cv2.createTrackbar("Val max","Track bar",255,255,np.empty)


while true:
    h_min=cv2.getTrackbarPos("Hue min","Track bar")
    h_max=cv2.getTrackbarPos("Hue max","Track bar")
    s_min=cv2.getTrackbarPos("Sat min","Track bar")
    s_max=cv2.getTrackbarPos("Sat max","Track bar")
    v_min=cv2.getTrackbarPos("Val min","Track bar")
    v_max=cv2.getTrackbarPos("Val max","Track bar")
    print(h_min,h_max,s_min,s_max,v_min,v_max)


    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(hsv,lower,upper)

    #bitwise_and將兩張圖片每一個bit做and運算
    #第二個img與第三個遮罩mask做bitwise and再回傳結果回第一個參數img
    result=cv2.bitwise_and(img,img,mask=mask)
    

    cv2.inRange(hsv,lower,upper)
    
    cv2.imshow("rgb",img)
    cv2.imshow("hsv",hsv)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    cv2.waitKey(1)

    
