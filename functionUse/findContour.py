import cv2

img=cv2.imread("shape.jpg")
imgContour=img.copy()#img.copy()複製一張img
#辨識邊緣只需要灰階影像不需用到彩色
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(img,150,200)


#findcontours回傳兩個值 第一個回傳輪廓座標 第二個回傳階層
contours,hierachy=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    #cv2.drawContours
    #參數:要畫的圖片,要畫的輪廓cnt,輪廓是第幾個(-1表示每個都畫),BRG顏色,線的粗度4
    cv2.drawContours(imgContour,cnt,-1,(255,0,0),4)
    

    #cv2.contourArea(cnt輪廓) 算面積
    areas=cv2.contourArea(cnt)
    print(cv2.contourArea(cnt))

    #cv2.arcLength(cnt,輪廓是否閉合)
    cv2.arcLength(cnt,True)

    

    if areas>500:
        #用多邊形近似形狀之輪廓
        peri=cv2.arcLength(cnt,True)

        #cnt為輪廓點,以peri*0.02當多邊形邊長,是否封閉
        vertices=cv2.approxPolyDP(cnt,peri*0.02,True)
        print(len(vertices))
        corners=len(vertices)#幾個頂點
        
        #boundingRect(bounding box)
        #x,y為左上角之座標 w,h為寬與高
        x,y,w,h=cv2.boundingRect(vertices)
        #要畫在哪,左上角座標,右下角座標,畫線顏色,線粗度
        cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),4)

        if corners ==3:
            cv2.putText(imgContour,"triangle",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        elif corners ==4:
            cv2.putText(imgContour,"rectangle",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

        elif corners ==5:
            cv2.putText(imgContour,"pentagon",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        elif corners >=6:
            cv2.putText(imgContour,"circle",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


cv2.imshow("fig1",img)
cv2.imshow("edge",canny)
cv2.imshow("imgContour",imgContour)
cv2.waitKey(0)
