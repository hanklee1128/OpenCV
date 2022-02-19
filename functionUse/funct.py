import cv2
import numpy as np

img=cv2.imread("dog.jpg")

#顏色轉換
#cv2.cvtColor(圖片變數,轉換的顏色)
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#模糊
#高斯模糊 kernal大小用tuple表示只能是基數 第三個參數為標準差
#kernel與標準差越大 照片越模糊
blurimg=cv2.GaussianBlur(img,(15,15),10)

#找圖片的輪廓
#圖片中像素值差距過大的兩個部分區隔出邊緣
#低於150就過濾掉不當邊緣來看,超過200就全部當成邊緣
cannyimg=cv2.Canny(img,150,200)


#dilate膨脹

kernel=np.ones((10,10),np.uint8)
#傳入參數 要傳入的圖片,要得kernel需求為一二D陣列,iterate幾次
dilateimg=cv2.dilate(cannyimg,kernel,iterations=1)
#kernel 2D陣列越大,iteration次數越大,則膨脹越明顯

#erode侵蝕 
erodeimg=cv2.erode(dilateimg,kernel,iterations=1)



cv2.imshow("fig1",img)
cv2.imshow("fig2",grayimg)
cv2.imshow("fig3",blurimg)
cv2.imshow("fig4",cannyimg)
cv2.imshow("fig5",dilateimg)
cv2.imshow("fig6",erodeimg)


cv2.waitKey(0)

